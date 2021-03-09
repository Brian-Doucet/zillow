#! python
#!/usr/bin/python3

"""Program to fetch data on sold homes from Zillow"""

import csv
import json
from typing import List, Union

from bs4 import BeautifulSoup
import requests

from models.zillow import ZillowAddress, ZillowData, ZillowRequest, ZillowAreaRequest
from utils import get_home_details, get_facts_and_features, build_request_parameters


class ZillowScraper():

    def __init__(self):
        self.results: List[ZillowData] = []
        self.output_file = 'zillow_listings.csv'

    def fetch(self, zillow_request: Union[ZillowRequest, ZillowAreaRequest]):
        print('REQUEST ', zillow_request)
        response = requests.get(url=zillow_request.get_url(),
                                headers=zillow_request.headers,
                                params=zillow_request.get_parameters())
        return response

    def get_zillow_urls_per_property(self, response_text) -> List[str]:
        list_of_urls = []
        content = BeautifulSoup(response_text, features='lxml')

        print('brek')
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
        print('Getting property details for ', url)
        zillow_request = ZillowRequest(url=url)
        response = self.fetch(zillow_request)
        content = BeautifulSoup(response.text, features='lxml')
        home_details = get_home_details(content)
        facts_features = get_facts_and_features(content)

        zillow_address = ZillowAddress(
            street_address=home_details.get("address").get("streetAddress"),
            city=home_details.get("address").get("addressLocality"),
            state=home_details.get("address").get("addressRegion"),
            zip_code=home_details.get("address").get("postalCode"),
            latitude=home_details.get("geo").get("latitude"),
            longitude=home_details.get("geo").get("longitude")
            )

        zillow_data_object = ZillowData(
            zpid=home_details.get("zpid"),
            property_name=home_details.get("name"),
            address=zillow_address,
            property_type=facts_features.get("home_type"),
            lot_size=facts_features.get("lot_size"),
            year_built=facts_features.get("year_built"),
            square_footage=home_details.get("floorSize").get("value"),
            total_interior_livable_area=facts_features.get("total_interior_livable_area"),
            price_per_sqft=facts_features.get("price/sqft"),
            stories=facts_features.get("stories"),
            foundation=facts_features.get("foundation"),
            roof=facts_features.get("roof"),
            new_construction=facts_features.get("new_construction"),
            bedrooms=facts_features.get("bedrooms"),
            bathrooms=facts_features.get("bathrooms"),
            full_bathrooms=facts_features.get("full_bathrooms"),
            flooring=facts_features.get("flooring"),
            basement=facts_features.get("basement"),
            fireplace=facts_features.get("fireplace"),
            parking=facts_features.get("parking"),
            garage=facts_features.get("has_garage"),
            garage_spaces=facts_features.get("garage_spaces"),
            heating=facts_features.get("heating"),
            cooling=facts_features.get("cooling"),
            hoa_dues=facts_features.get("hoa"),
            tax_assessed_value=facts_features.get("tax_assessed_value"),
            annual_tax_amount=facts_features.get("annual_tax_amount"),
            property_url=home_details.get("url")
            )

        return zillow_data_object

    def write_to_csv(self):
        with open(self.output_file, 'w') as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=self.results[0].header_fields())
            writer.writeheader()

            for row in self.results:
                writer.writerow(row.dict())

    def run(self):
        target_area = "porter-square-ma"
        params = build_request_parameters(target_area)
        request = ZillowAreaRequest(target_area=target_area, params=params)
        response = self.fetch(request)
        urls = self.get_zillow_urls_per_property(response.text)
        url_to_search_for = urls[9]
        self.results.append(self.get_property_details(url_to_search_for))
        self.write_to_csv()


# if __name__ == '__main__':
#     scraper = ZillowScraper()
#     scraper.run()


def simple_test():
    scraper = ZillowScraper()
    target_area = 'porter-square-ma'
    params = build_request_parameters(" ".join(target_area.split("-")))
    request = ZillowAreaRequest(target_area=target_area, params=params)


    response = scraper.fetch(request)
    searchResults = response.json()["searchResults"]

    print(len(searchResults))


simple_test()