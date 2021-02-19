import requests
from bs4 import BeautifulSoup
import json

from utils import ZILLOW_URL, ZILLOW_QUERY_HEADERS, ZILLOW_QUERY_PARAMS


class ZillowScraper():

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
                print(property_data_json)

    def run(self):
        url = ZILLOW_URL
        params = ZILLOW_QUERY_PARAMS
        headers = ZILLOW_QUERY_HEADERS

        response = self.fetch(url=url, params=params, headers=headers)
        self.parse(response.text)


if __name__ == '__main__':
    scraper = ZillowScraper()
    scraper.run()
