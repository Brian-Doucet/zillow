#!/usr/bin/python3

"""Program to fetch data on sold homes from Zillow"""

import csv
import json
from typing import List

from bs4 import BeautifulSoup
import requests
from models.zillow import ZillowResponse, ZillowRequest

from constants import ZILLOW_URL, ZILLOW_QUERY_HEADERS, ZILLOW_QUERY_PARAMS


class ZillowScraper():

    def __init__(self):
        self.results: List[ZillowResponse] = []
        self.output_file = 'zillow_listings.csv'

    def fetch(self, zillow_request: ZillowRequest):
        response = requests.get(zillow_request.url,
                                headers=zillow_request.headers,
                                params=zillow_request.params)

        print(response)
        return response

    def parse(self, response):
        content = BeautifulSoup(response, features='lxml')
        property_cards = content.find(
            'ul', {'class': 'photo-cards photo-cards_wow photo-cards_short'})
        for child_property in property_cards:
            property_data = child_property.find(
                'script', {'type': 'application/ld+json'})
            if property_data:
                property_data_json = json.loads(property_data.contents[0])

                zillow_response = ZillowResponse(
                    full_address=property_data_json['name'],
                    street_name=property_data_json['address']['streetAddress'],
                    state=property_data_json['address']['addressRegion'],
                    zip_code=property_data_json['address']['postalCode'],
                    property_url=property_data_json['url'],
                    square_footage=property_data_json['floorSize']['value'],
                    sales_prices=child_property.find('div', {'class': 'list-card-price'}).text
                )

                self.results.append(zillow_response)

    def write_to_csv(self):
        with open(self.output_file, 'w') as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=self.results[0].header_fields())
            writer.writeheader()

            for row in self.results:
                writer.writerow(row.dict())

    def run(self):

        request = ZillowRequest(
            url=ZILLOW_URL,
            params=ZILLOW_QUERY_PARAMS,
            headers=ZILLOW_QUERY_HEADERS
        )

        response = self.fetch(request)
        self.parse(response.text)
        self.write_to_csv()


if __name__ == '__main__':
    scraper = ZillowScraper()
    scraper.run()
