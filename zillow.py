#!/usr/bin/python3

"""Program to fetch data on sold homes from Zillow"""

import csv
import json
from bs4 import BeautifulSoup
import requests

from utils import ZILLOW_URL, ZILLOW_QUERY_HEADERS, ZILLOW_QUERY_PARAMS


class ZillowScraper():
    results = []

    def fetch(self, url, params, headers):
        response = requests.get(url, headers=headers, params=params)
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

                # extract details for each listing
                self.results.append({"full_address": property_data_json['name'],
                                     "street_name": property_data_json['address']['streetAddress'],
                                     "state": property_data_json['address']['addressRegion'],
                                     "zip_code": property_data_json['address']['postalCode'],
                                     "property_url": property_data_json['url'],
                                     "square_footage": property_data_json['floorSize']['value'],
                                     'sales_price': child_property.find('div', {'class': 'list-card-price'}).text})

    def to_csv(self):
        with open('zillow_listings.csv', 'w') as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()

            for row in self.results:
                writer.writerow(row)

    def run(self):
        url = ZILLOW_URL
        params = ZILLOW_QUERY_PARAMS
        headers = ZILLOW_QUERY_HEADERS

        response = self.fetch(url=url, params=params, headers=headers)
        self.parse(response.text)
        self.to_csv()


if __name__ == '__main__':
    scraper = ZillowScraper()
    scraper.run()
