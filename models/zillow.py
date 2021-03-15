from typing import Optional, Dict, Any

from pydantic import BaseModel

from constants import ZILLOW_URL, ZILLOW_QUERY_PARAMS, ZILLOW_QUERY_HEADERS

class ZillowAddress(BaseModel):


    def header_fields(self):
        return self.__fields__

class ZillowData(BaseModel):
    zpid: Optional[str]
    property_url: Optional[str]
    property_name: Optional[str]
    street_address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    latitude: Optional[str]
    longitude:Optional[str]
    #address:Optional[ZillowAddress]
    property_type: Optional[str]
    lot_size: Optional[str]
    year_built: Optional[str]
    square_footage: Optional[str]
    total_interior_livable_area: Optional[str]
    price_per_sqft: Optional[str]
    stories: Optional[str]
    foundation: Optional[str]
    roof: Optional[str]
    new_construction:Optional[str]
    bedrooms:Optional[str]
    bathrooms:Optional[str]
    full_bathrooms: Optional[str]
    flooring: Optional[str]
    basement: Optional[str]
    fireplace: Optional[str]
    parking: Optional[str]
    garage: Optional[str]
    garage_spaces: Optional[str]
    heating: Optional[str]
    cooling: Optional[str]
    hoa_dues: Optional[str]
    tax_assessed_value: Optional[str]
    annual_tax_amount: Optional[str]
    sale_price: Optional[str]

    def header_fields(self):
        return self.__fields__




class ZillowRequest(BaseModel):
    url: Optional[str] = ZILLOW_URL
    params: Optional[Dict] = ZILLOW_QUERY_PARAMS
    headers: Optional[Dict] = ZILLOW_QUERY_HEADERS

    def add_params(self, params:dict):
        self.params.update(params)

