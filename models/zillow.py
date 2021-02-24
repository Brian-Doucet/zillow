from typing import Optional, Dict, Any

from pydantic import BaseModel

from constants import ZILLOW_URL, ZILLOW_QUERY_PARAMS, ZILLOW_QUERY_HEADERS


class ZillowData(BaseModel):
    name: Optional[str]
    type: Optional[str]
    number_of_rooms: Optional[str]
    address: Optional[Any] #remodel this to be of class Address
    street_name: Optional[Any]
    state: Optional[str]
    zip_code: Optional[str]
    property_url: Optional[str]
    square_footage: Optional[str]
    sales_prices: Optional[str]

    def header_fields(self):
        return self.__fields__


class Address(BaseModel):
    """
    TODO: capture all the fields based on the following data
    'address': {'@type': 'PostalAddress', '@context': 'http://schema.org', 'streetAddress': '3903 Perkins Rd', 'addressLocality': 'Thompsons Station', 'addressRegion': 'TN', 'postalCode': '37179'}
    """
    pass


class ZillowRequest(BaseModel):
    url: Optional[str] = ZILLOW_URL
    params: Optional[Dict] = ZILLOW_QUERY_PARAMS
    headers: Optional[Dict] = ZILLOW_QUERY_HEADERS

    def add_params(self, params:dict):
        self.params.update(params)

