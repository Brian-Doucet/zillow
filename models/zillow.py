from typing import Optional, Dict
import json

from pydantic import BaseModel

from constants import ZILLOW_URL, ZILLOW_QUERY_PARAMS, ZILLOW_QUERY_HEADERS


class ZillowAddress(BaseModel):
    street_address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]

    def header_fields(self):
        return self.__fields__


class ZillowData(BaseModel):
    zpid: Optional[str]
    property_url: Optional[str]
    property_name: Optional[str]
    address: Optional[ZillowAddress]
    property_type: Optional[str]
    lot_size: Optional[str]
    year_built: Optional[str]
    square_footage: Optional[str]
    total_interior_livable_area: Optional[str]
    price_per_sqft: Optional[str]
    stories: Optional[str]
    foundation: Optional[str]
    roof: Optional[str]
    new_construction: Optional[str]
    bedrooms: Optional[str]
    bathrooms: Optional[str]
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


class ZillowParams(BaseModel):
    pagination: Dict[str, int] = {"currentPage": 1}
    # usersSearchTerm: Optional[str]
    mapBounds: Dict[str, float]
    MapVisible: bool = False
    sort: Dict[str, str] = {"value": "globalrelevance"}
    isListVisible: bool = True
    # filterState = {"doz": {"value": "24m"},
    #                "pmf": {"value": False}, "fore": {"value": False}, "ah": {"value": True}, "auc": {"value": False},
    #                "nc": {"value": False}, "rs": {"value": True}, "fsbo": {"value": False}, "cmsn": {"value": False},
    #                "pf": {"value": False}, "fsba": {"value": False}, "sort": {"value": "globalrelevanceex"}}


class ZillowRequest(BaseModel):
    _base_url: str = 'https://www.zillow.com'
    url: Optional[str] = ZILLOW_URL
    params: Optional[Dict] = ZILLOW_QUERY_PARAMS
    headers: Optional[Dict] = ZILLOW_QUERY_HEADERS

    def add_params(self, params: dict):
        self.params.update(params)

    def get_url(self):
        return self.url

    def get_parameters(self):
        return self.params


class ZillowAreaRequest(BaseModel):
    _base_url: str = 'https://www.zillow.com'
    target_area: Optional[str]
    headers: Optional[Dict] = ZILLOW_QUERY_HEADERS
    category: Optional[str]
    params: ZillowParams

    def get_url(self):
        return f'{self._base_url}/search/GetSearchPageState.htm'

    def get_parameters(self):
        val = {"searchQueryState": json.dumps(self.params.dict())}
        print('PARAMETERS ', val)
        return val
