ZILLOW_URL = 'https://www.zillow.com/thompsons-station-tn/sold/'
ZILLOW_QUERY_PARAMS = {
    "searchQueryState": '{"pagination":{"currentPage":1},"usersSearchTerm":"Thompsons Station, TN","mapBounds":{"west":-87.1425982001953,"east":-86.66881279980467,"south":35.646757343441735,"north":35.99806935769734},"mapZoom":11,"regionSelection":[{"regionId":29482,"regionType":6}],"isMapVisible":false,"filterState":{"doz":{"value":"24m"},"pmf":{"value":false},"fore":{"value":false},"ah":{"value":true},"auc":{"value":false},"nc":{"value":false},"rs":{"value":true},"fsbo":{"value":false},"cmsn":{"value":false},"pf":{"value":false},"fsba":{"value":false},"sort":{"value":"globalrelevanceex"}},"isListVisible":true}'
}

ZILLOW_QUERY_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'zguid=23|%24e72fcfc5-847e-491a-85bc-b8a15038fd65; zgsession=1|c3b828b1-5797-4ded-9259-d5853d01a633; _ga=GA1.2.724605297.1613482749; zjs_user_id=null; zjs_anonymous_id=%22e72fcfc5-847e-491a-85bc-b8a15038fd65%22; _gcl_au=1.1.1407950069.1613482749; KruxPixel=true; DoubleClickSession=true; _pxvid=58a8e6fd-705c-11eb-a64b-0242ac120006; _fbp=fb.1.1613482749307.389903904; KruxAddition=true; ki_r=; ki_s=211289%3A0.0.0.0.0; _pin_unauth=dWlkPVlqUTBNakF5WlRRdE5XRmpaQzAwWW1WakxUZzJNVEl0T1RrMlpqVTVPRGRtWWpreQ; ki_t=1613482839306%3B1613482839306%3B1613492721948%3B1%3B153; _gid=GA1.2.517665822.1613677646; _derived_epik=dj0yJnU9X0NlWmlkTldsWHczRHAzLVZQakpqUGtaZERHaVYyU0wmbj1uM05rdFhOXzlNN05GNHFYOEE2cVR3Jm09NyZ0PUFBQUFBR0F1eEU0; _uetsid=20e0f800722211eba07455463f10c860; _uetvid=58b92890705c11eb89a239317bdfc177; _px3=41d7b3cf36bfe337c9695b3031d1021f1fb4cdaaefb4a76620177e0058d7ce25:COI5mw5uoLloAArF1TIv0dqpor5qhLuGIqfGwtHEiiwfFhSLI5GEZjTX6kF4KOlaMp/1DLJ0hVB6JxKFoKdPbg==:1000:+oFMKFquPY3Mezk5MrvsEU0tiUfxponawnEg9U/U5SDuXYfYzVbABJ1G4gvpa5eCMhUgnvJ3D90n3gmFWJGCBQqmhx6CrGy0GZEVvR/5tzQVBBCNojifg5zizu2Du7Aj0pZz2KTULmMIKSsPhrTSMNJklsyjYj8Hi6IVoApyHsw=; AWSALB=7toHjQvgnYmO8EVADkYgLNND1oCkPZl9f+eAukV+Gn0u1ja0SkkKl14U5SP91eoeZ7jEZqeFWmOA4GJcrQ4wcsJqqqyHzbXAf6WSCgudktdECfXEMw79JbycqqsK; AWSALBCORS=7toHjQvgnYmO8EVADkYgLNND1oCkPZl9f+eAukV+Gn0u1ja0SkkKl14U5SP91eoeZ7jEZqeFWmOA4GJcrQ4wcsJqqqyHzbXAf6WSCgudktdECfXEMw79JbycqqsK; JSESSIONID=AC25408DCAF1874539FDE494E3A1BC97; search=6|1616272946344%7Crect%3D35.99806935769734%252C-86.66881279980467%252C35.646757343441735%252C-87.1425982001953%26rid%3D29482%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26days%3D24m%26fs%3D0%26fr%3D0%26mmm%3D0%26rs%3D1%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0929482%09%09%09%09%09%09',
    'referer': 'https://www.zillow.com/homes/Thompsons-Station,-TN_rb/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
