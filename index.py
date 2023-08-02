import requests
import json
from requests_html import HTMLSession
from uuid import uuid4

session = HTMLSession()

def bigwheelburgerFeatures():
    text = ""
    html = session.get("https://bigwheelburger.com/menu/").html
    features = html.find('.single-feature')
    for feature in features:
        text += "- {} \n".format(feature.text)

    return text

def chocolatfavoris():
    expectedFlavours = [
        "Classic Dip Cone",
        "Cotton Candy",
        "S'mores",
        "Cookies & Cream",
        "Dulce de Leche",
        "Original Milk",
        "Salted Caramel",
        "Hazelnut Praline",
        "Classic Dark Chocolate",
        "Crunchy Hazelnut",
        "Tanzania 75%"
    ]

    text = ""
    url = "https://api.ueat.io/graphql"

    payload = json.dumps({
      "operationName": "items",
      "variables": {
        "categoryId": 29615,
        "orderType": "TAKEOUT",
        "franchiseCode": "110",
        "expectedDate": None
      },
      "query": "query items($categoryId: Int!) {items(categoryId: $categoryId) {  name }}"
    })
    headers = {
      'content-type': 'application/json',
      'x-ueatapikey': 'ff376cab-30e2-4cce-9999-ed755583c7f5',
      'x-ueatculture': 'en-CA',
      'x-ueatsessionid': 'e317f902-598c-4c45-a629-13fcc68d260c',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    allFlavours = map(lambda flavour: flavour['name'], json.loads(response.text)['data']['items'])
    flavours = filter(lambda flavour: flavour not in expectedFlavours, allFlavours)

    for flavour in flavours:
        text += "- {} \n".format(flavour)

    return text

print()
print("# Big Wheel Burger")
print(bigwheelburgerFeatures())
print("# Chocolat Favoris (Special Dips)")
print(chocolatfavoris())
