from typing import List

from pydantic import BaseModel, root_validator


class Geolocation(BaseModel):
    boundingbox: List[str]
    display_name: str
    lon: str
    lat: str
    east: str
    west: str
    north: str
    south: str

    @root_validator(pre=True)
    def parse_values(cls, values):
        bounding_box: List[str] = values['boundingbox']
        values['west'], values['east'], values['north'], values['south'] = bounding_box
        return values

    def get_map_bounds(self):
        return {
            "west": self.west,
            "east": self.east,
            "north": self.north,
            "south": self.south
        }
