#!/usr/bin/python3

"""Program to fetch data on sold homes from Zillow"""

import csv
import json
from typing import List

from bs4 import BeautifulSoup
import requests
from models.zillow import ZillowData, ZillowRequest


class ZillowScraper():

    def __init__(self):
        self.results: List[ZillowData] = []
        self.output_file = 'zillow_listings.csv'

    def fetch(self, zillow_request: ZillowRequest):
        response = requests.get(url=zillow_request.url,
                                headers=zillow_request.headers,
                                params=zillow_request.params)

        return response

    def get_zillow_urls_per_property(self, response) -> List[str]:
        list_of_urls = []
        content = BeautifulSoup(response, features='lxml')

        property_cards = content.find(
            'ul', {'class': 'photo-cards photo-cards_wow photo-cards_short'}
        )

        for child_property in property_cards:
            property_data = child_property.find(
                'script', {'type': 'application/ld+json'}
            )

            if property_data:
                property_data_json = json.loads(property_data.contents[0])

                list_of_urls.append(
                    property_data_json['url']
                )

        return list_of_urls

    def get_property_details(self, url: str) -> ZillowData:

        zillow_request = ZillowRequest(url=url)
        response = self.fetch(zillow_request)
        content = BeautifulSoup(response.text, features='lxml')
        json_text = json.loads(content.find_all(
            "script", {"type": "application/ld+json"})[1].string)
        print(json_text)
        zillow_data_object = ZillowData(
            property_type=json_text['@type'],
            property_name=json_text['name'],
            number_of_rooms=json_text['numberOfRooms'],
            address=json_text['address'],
            property_url=json_text['url']
        )

        return zillow_data_object

    def parse(self, response):
        content = BeautifulSoup(response, features='lxml')
        property_cards = content.find(
            'ul', {'class': 'photo-cards photo-cards_wow photo-cards_short'})
        for child_property in property_cards:
            property_data = child_property.find(
                'script', {'type': 'application/ld+json'})
            if property_data:
                property_data_json = json.loads(property_data.contents[0])

                url_for_property = property_data_json['url']

                follow_up_request = ZillowRequest(url=url_for_property)
                response = self.fetch(follow_up_request)

                content = BeautifulSoup(response.text, features='lxml')

                break

                # zillow_response = ZillowData(
                #     full_address=property_data_json['name'],
                #     street_name=property_data_json['address']['streetAddress'],
                #     state=property_data_json['address']['addressRegion'],
                #     zip_code=property_data_json['address']['postalCode'],
                #     property_url=property_data_json['url'],
                #     square_footage=property_data_json['floorSize']['value'],
                #     sales_prices=child_property.find('div', {'class': 'list-card-price'}).text
                # )
                #
                # self.results.append(zillow_response)

    def write_to_csv(self):
        with open(self.output_file, 'w') as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=self.results[0].header_fields())
            writer.writeheader()

            for row in self.results:
                writer.writerow(row.dict())

    def run(self):

        request = ZillowRequest()

        response = self.fetch(request)
        urls = self.get_zillow_urls_per_property(response.text)
        self.results.append(self.get_property_details(urls[0]))
        self.write_to_csv()


if __name__ == '__main__':
    scraper = ZillowScraper()
    scraper.run()
