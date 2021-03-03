from typing import Optional, Dict, Any

from pydantic import BaseModel

from constants import ZILLOW_URL, ZILLOW_QUERY_PARAMS, ZILLOW_QUERY_HEADERS


class ZillowData(BaseModel):
    property_name: Optional[str]
    property_type: Optional[str]
    square_footage: Optional[str]
    number_of_rooms: Optional[str]
    year_built: Optional[str]
    heating: Optional[str]
    cooling: Optional[str]
    parking: Optional[str]
    lot_size: Optional[str]
    price_per_sqft: Optional[str]
    hoa_dues: Optional[str]
    sale_price: Optional[str]
    property_url: Optional[str]
    zpid: Optional[str]

    def header_fields(self):
        return self.__fields__


class Address(BaseModel):
    street_address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]

    def header_fields(self):
        return self.__fields__


class ZillowRequest(BaseModel):
    url: Optional[str] = ZILLOW_URL
    params: Optional[Dict] = ZILLOW_QUERY_PARAMS
    headers: Optional[Dict] = ZILLOW_QUERY_HEADERS

    def add_params(self, params:dict):
        self.params.update(params)

