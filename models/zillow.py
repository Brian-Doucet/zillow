from typing import Optional, Dict

from pydantic import BaseModel


class ZillowResponse(BaseModel):
    full_address: Optional[str]
    street_name: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    property_url: Optional[str]
    square_footage: Optional[str]
    sales_prices: Optional[str]

    def header_fields(self):
        return self.__fields__


class ZillowRequest(BaseModel):
    url: Optional[str]
    params: Optional[Dict]
    headers: Optional[Dict]
