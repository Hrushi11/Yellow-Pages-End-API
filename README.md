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

![IMG](https://github.com/Hrushi11/Yellow-Pages-End-API/blob/main/assets/plier_code.png?raw=true)

## API Data

First 2 samples from this route: `http://hrushis-yellow-pages-end-api.herokuapp.com/repair/texas/5` are shown here. <br>
The key contains the number and the value contains the actual data in a nested dictionary. The keys in the dictionary and there values are well explained below.

`Address`: The address of the entity included in the call. <br>
`Categories`: To what types of other services the entity is in. <br>
`More-info` : To get more information about the entity on the yellow pages website <br>
`Name`: Name of the entity. <br>
`Phone-number`: Telephone number for contacting the entity. <br>
`Status`: Opened or Closed status of the entity. <br>
`Website`: Own website of the enitity. <br>

`null`: Data for that key was not available. <br>

```
{
  "1": {
    "Address": null,
    "Categories": [
      "Auto Repair & Service",
      "Tire Dealers"
    ],
    "More-info": "https://www.yellowpages.com/nationwide/mip/firestone-complete-auto-care-497692017?lid=1001662607171",
    "Name": "Firestone Complete Auto Care",
    "Phone-number": "(800) 364-4314",
    "Status": null,
    "Website": "http://www.firestonecompleteautocare.com/repair/services.jsp?lw_cmp=IYP_YPC_NPLL_Service"
  },
  "2": {
    "Address": null,
    "Categories": [
      "Auto Repair & Service",
      "Automobile Salvage",
      "Automobile & Truck Brokers"
    ],
    "More-info": "https://www.yellowpages.com/nationwide/mip/1-800-car-buyers-481040864?lid=1000123041450",
    "Name": "1 800 Car Buyers",
    "Phone-number": "(888) 495-3593",
    "Status": null,
    "Website": "http://www.800carbuyers.com/?st-t=yp-carbuyer"
  }
}
```
