# Yellow Pages API

This repository contains the code for completely scraping the yellow pages website to get the details of all the categories from all the cities in America and 
then turning all of the data into an api to be used later. The api data is well visualized here as example [here](https://github.com/Hrushi11/Yellow-Pages-End-API/tree/main/Yellow-pages).

Test the API at: [API Testing](https://hrushis-yellow-pages-end-api.herokuapp.com/)

![GIF](https://github.com/Hrushi11/Yellow-Pages-End-API/blob/main/assets/api-testing.gif?raw=true)

## Using the API

There are 2 different routes available for this api. One withour plier and another with plier. <br>

`plier`: Every website can not contain all the details on a single page, to overcome this multiple pages are used which hold around 30 cards of data. So every plier
you include, it is a multiple of 30 to get the number of data.

The following images show with code how to get the data from this api. A live testing route is already available [here](https://hrushis-yellow-pages-end-api.herokuapp.com/).

![IMG](https://github.com/Hrushi11/Yellow-Pages-End-API/blob/main/assets/without_plier_code.png?raw=true)

```
import requests
from yellow_pages_api import YpApi

# using the api with plier
api = YpApi()
search_term = "dentist"
geo_location_term = "texas"
plier = 3
# get the json request
url = f"https://hrushis-yellow-pages-end-api.herokuapp.com/{search_term}/{geo_location_term}/{plier}"
json_req = requests.get(url).json()
print(json_req)
```

![IMG](https://github.com/Hrushi11/Yellow-Pages-End-API/blob/main/assets/plier_code.png?raw=true)
