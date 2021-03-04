#!/usr/bin/python3

"""Set of functions for parsing HTML from Zillow"""
import json
import re

from bs4 import BeautifulSoup

# HTML output from an example property listing. Saves sending repeated requests
# when testing these functions.
sample_listing_html = open("zillow_sample.txt", "r", encoding='utf-8').read()
content = BeautifulSoup(sample_listing_html, "lxml")

def get_zillow_property_id(url):
    """Get the unique identifier for each property listing on Zillow.

    Args:
        url (str): Zillow URL for a specific listing

    Returns:
        str: Zillow property id
    """
    pattern = re.compile(r"(\d+)_zpid")
    zpid = re.search(pattern, url).group(1)

    return zpid

def get_home_details(content):
    """Get basic details of a property listing on Zillow

    Args:
        content (str): HTML from the home details page of a specific listing

    Returns:
        Dict: A dictionary of JSON data

    Data values include:
    =============   ==========================================================
    Property Type   The type of property (e.g. Single Family Residence).
    Property Name   The name of the property as it appears on the listing page.
    Zillow ID       Unique identifier on Zillow for each property listing.
    Square Footage  The total area of the home, measured in feet.
    # of Rooms      Total number rooms.
    Geo Coordinates Both the latitude and longitude of the property.
    URL             The URL for each property listing.
    Full Address    Includes number, street name, city, state, zip code.
    Street Address  The street address portion only (e.g 123 Green Street).
    City            The name of the city.
    State           State abbreviation (e.g. TN for Tennessee).
    Zip Code        US only. Zillow does not publish international listings.
    """
    property_details = content.find('script', {'type': 'application/ld+json'}).string
    property_details_json = json.loads(property_details)
    zillow_property_id = get_zillow_property_id(property_details_json.get("url"))
    property_details_json["zpid"] = zillow_property_id
    
    return property_details_json

def get_facts_and_features(content):
    """Get data from the facts and features section of the property listing.
    Not all listings will include these features.

    Args:
        content (str): HTML from the home details page of a property listing

    Returns:
        Dict: A dictionary of property features
    
    Data values include:
    =============   ==========================================================
    Type          Property type category (e.g. Townhouse, MultiFamily).
    Year Built    Four-digit year representing when the property was built.
    Price/sqft    Price divided by the square footage.
    Lot Size      Total size of the lot, measured in acres.
    Heating       The source used for heating (e.g. Central).
    Cooling       The source used to cool the property, if any (e.g. Central Air).
    Parking       Type of parking available (e.g. Garage Faces Front)
    HOA           Homeowner's association dues, if any.
    """
    facts_features = [feature.get_text() 
                      for feature in content.find('ul', {'class': 'ds-home-fact-list'})
                     ]
    k = [f.split(":")[0] for f in facts_features]
    val = [f.split(":")[1] for f in facts_features]
    features_dict = dict(zip(k, val))
    
    return features_dict

# Example to show the output
details = get_home_details(content)
features = get_facts_and_features(content)
zpid = get_zillow_property_id(details.get("url"))

print(details, "\n")
print(features, "\n")
print(zpid, "\n")
