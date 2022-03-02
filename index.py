import requests
import json
from requests_html import HTMLSession

session = HTMLSession()

def bigwheelburgerFeatures():
    text = ""
    html = session.get("https://bigwheelburger.com/menu/").html
    features = html.find('.single-feature')
    for feature in features:
        text += feature.text + "\n"

    return text

def chocolatefavoris():
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
      'x-ueatsessionid': 'df3038b6-cd5f-4507-899e-e68f0c6a14cc'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    allFlavours = map(lambda flavour: flavour['name'], json.loads(response.text)['data']['items'])
    flavours = filter(lambda flavour: flavour not in expectedFlavours, allFlavours)

    for flavour in flavours:
        text += flavour + "\n"

    return text

print()
print("# bigwheelburger")
print(bigwheelburgerFeatures())
print("# chocolate favoris special dips")
print(chocolatefavoris())
