# Import libraries
import requests
import csv
import time
import json


### API_KEY = ""

# for testing only
# data1 = {
#     "name": "places/ChIJV4H1Z1bzWYgRghpzZZmH6J4",
#     "id": "ChIJV4H1Z1bzWYgRghpzZZmH6J4",
#     "types": [
#             "consultant",
#             "accounting",
#         "finance",
#         "point_of_interest",
#         "establishment"
#     ],
#     "nationalPhoneNumber": "(828) 505-3963",
#     "internationalPhoneNumber": "+1 828-505-3963",
#     "formattedAddress": "107 Merrimon Ave STE 120, Asheville, NC 28801, USA",
#     "addressComponents": [
#         {
#             "longText": "STE 120",
#             "shortText": "STE 120",
#             "types": [
#                 "subpremise"
#             ],
#             "languageCode": "en"
#         },
#         {
#             "longText": "107",
#             "shortText": "107",
#             "types": [
#                 "street_number"
#             ],
#             "languageCode": "en-US"
#         },
#         {
#             "longText": "Merrimon Avenue",
#             "shortText": "Merrimon Ave",
#             "types": [
#                 "route"
#             ],
#             "languageCode": "en"
#         },
#         {
#             "longText": "Asheville",
#             "shortText": "Asheville",
#             "types": [
#                 "locality",
#                 "political"
#             ],
#             "languageCode": "en"
#         },
#         {
#             "longText": "Buncombe County",
#             "shortText": "Buncombe County",
#             "types": [
#                 "administrative_area_level_2",
#                 "political"
#             ],
#             "languageCode": "en"
#         },
#         {
#             "longText": "North Carolina",
#             "shortText": "NC",
#             "types": [
#                 "administrative_area_level_1",
#                 "political"
#             ],
#             "languageCode": "en"
#         },
#         {
#             "longText": "United States",
#             "shortText": "US",
#             "types": [
#                 "country",
#                 "political"
#             ],
#             "languageCode": "en"
#         },
#         {
#             "longText": "28801",
#             "shortText": "28801",
#             "types": [
#                 "postal_code"
#             ],
#             "languageCode": "en-US"
#         }
#     ],
#     "location": {
#         "latitude": 35.6028786,
#         "longitude": -82.5525724
#     },
#     "rating": 5,
#     "googleMapsUri": "https://maps.google.com/?cid=11450551145491274370",
#     "regularOpeningHours": {
#         "openNow": False,
#         "periods": [
#             {
#                 "open": {
#                     "day": 1,
#                     "hour": 9,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 1,
#                     "hour": 16,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 2,
#                     "hour": 9,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 2,
#                     "hour": 16,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 3,
#                     "hour": 9,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 3,
#                     "hour": 16,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 4,
#                     "hour": 9,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 4,
#                     "hour": 16,
#                     "minute": 0
#                 }
#             },
#             {
#                 "open": {
#                     "day": 5,
#                     "hour": 9,
#                     "minute": 0
#                 },
#                 "close": {
#                     "day": 5,
#                     "hour": 16,
#                     "minute": 0
#                 }
#             }
#         ],
#         "weekdayDescriptions": [
#             "Monday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Tuesday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Wednesday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Thursday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Friday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Saturday: Closed",
#             "Sunday: Closed"
#         ]
#     },
#     "utcOffsetMinutes": -240,
#     "userRatingCount": 3,
#     "displayName": {
#         "text": "Brian D Henderson CPA PA",
#         "languageCode": "en"
#     },
#     "primaryTypeDisplayName": {
#         "text": "Consultant",
#         "languageCode": "en-US"
#     },
#     "currentOpeningHours": {
#         "openNow": False,
#         "periods": [
#             {
#                 "open": {
#                     "day": 1,
#                     "hour": 9,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 13
#                     }
#                 },
#                 "close": {
#                     "day": 1,
#                     "hour": 16,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 13
#                     }
#                 }
#             },
#             {
#                 "open": {
#                     "day": 2,
#                     "hour": 9,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 14
#                     }
#                 },
#                 "close": {
#                     "day": 2,
#                     "hour": 16,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 14
#                     }
#                 }
#             },
#             {
#                 "open": {
#                     "day": 3,
#                     "hour": 9,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 15
#                     }
#                 },
#                 "close": {
#                     "day": 3,
#                     "hour": 16,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 15
#                     }
#                 }
#             },
#             {
#                 "open": {
#                     "day": 4,
#                     "hour": 9,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 9
#                     }
#                 },
#                 "close": {
#                     "day": 4,
#                     "hour": 16,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 9
#                     }
#                 }
#             },
#             {
#                 "open": {
#                     "day": 5,
#                     "hour": 9,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 10
#                     }
#                 },
#                 "close": {
#                     "day": 5,
#                     "hour": 16,
#                     "minute": 0,
#                     "date": {
#                         "year": 2024,
#                         "month": 5,
#                         "day": 10
#                     }
#                 }
#             }
#         ],
#         "weekdayDescriptions": [
#             "Monday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Tuesday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Wednesday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Thursday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Friday: 9:00\u202fAM\u2009\u2013\u20094:00\u202fPM",
#             "Saturday: Closed",
#             "Sunday: Closed"
#         ]
#     },
#     "primaryType": "consultant",
#     "shortFormattedAddress": "107 Merrimon Ave STE 120, Asheville",
#     "reviews": [
#         {
#             "name": "places/ChIJV4H1Z1bzWYgRghpzZZmH6J4/reviews/ChZDSUhNMG9nS0VJQ0FnSUNvdjhqSVB3EAE",
#             "relativePublishTimeDescription": "5 years ago",
#             "rating": 5,
#             "authorAttribution": {
#                     "displayName": "Greta Dean",
#                     "uri": "https://www.google.com/maps/contrib/115341775633105119529/reviews",
#                     "photoUri": "https://lh3.googleusercontent.com/a-/ALV-UjUG4gwtLaY2kP5pjFbQWZt-qpUUcUv6vHNnU2dCtTddgEo1PJGw=s128-c0x00000000-cc-rp-mo"
#             },
#             "publishTime": "2019-03-05T13:00:52Z"
#         },
#         {
#             "name": "places/ChIJV4H1Z1bzWYgRghpzZZmH6J4/reviews/ChZDSUhNMG9nS0VJQ0FnSUNLNjVXMUx3EAE",
#             "relativePublishTimeDescription": "3 years ago",
#             "rating": 5,
#             "authorAttribution": {
#                     "displayName": "Camille DeWinters",
#                     "uri": "https://www.google.com/maps/contrib/116335410024031129434/reviews",
#                     "photoUri": "https://lh3.googleusercontent.com/a-/ALV-UjUKbOntFHN2sLZpwc396G58ar0vRPOusOYuWiQWijefmM_rg64=s128-c0x00000000-cc-rp-mo"
#             },
#             "publishTime": "2021-04-19T17:13:30Z"
#         },
#         {
#             "name": "places/ChIJV4H1Z1bzWYgRghpzZZmH6J4/reviews/ChZDSUhNMG9nS0VJQ0FnSURvZ2QtOEhBEAE",
#             "relativePublishTimeDescription": "5 years ago",
#             "rating": 5,
#             "authorAttribution": {
#                     "displayName": "Philip Lewis (Eyecon Imaging)",
#                     "uri": "https://www.google.com/maps/contrib/107505303855376493386/reviews",
#                     "photoUri": "https://lh3.googleusercontent.com/a-/ALV-UjWtvhWsrQP5WeEbT-G-kRlDueaxjgIr1o2ueQ7G3YBgRyEFQCOi=s128-c0x00000000-cc-rp-mo"
#             },
#             "publishTime": "2019-03-18T16:12:31Z"
#         }
#     ]
# }


central_location = "28801"
search_radius = "1000"
company_characteristics = "CPA"
max_loop_count = 6
sleep_time_seconds = 30
filename = "business_results.csv"
testfile = "test.csv"

# Initialize variables
all_results = []
next_page_token = "initial"


# keys = ['addressComponents', 'currentOpeningHours', 'displayName', 'editorialSummary', 'formattedAddress',
#         'googleMapsUri', 'id', 'location', 'name', 'nationalPhoneNumber', 'priceLevel', 'primaryType',
#         'primaryTypeDisplayName', 'rating', 'regularOpeningHours', 'reviews', 'shortFormattedAddress',
#         'subDestinations', 'types', 'userRatingCount', 'utcOffsetMinutes', 'websiteUri']
keys = [
    # 'addressComponents',
    # 'currentOpeningHours',
    'displayName',
    'rating',
    'userRatingCount',
    'types',
    'websiteUri',
    'nationalPhoneNumber',
    'formattedAddress',
    'googleMapsUri',
    # 'location',
    'name',
    'id',
    'primaryType',
    # 'primaryTypeDisplayName',

    # 'regularOpeningHours',
    # 'reviews',
    # 'shortFormattedAddress',
    # 'subDestinations',
    'priceLevel',
    'utcOffsetMinutes',
    'editorialSummary'
]

# Function to geocode address


def geocode_address(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        latitude = data["results"][0]["geometry"]["location"]["lat"]
        longitude = data["results"][0]["geometry"]["location"]["lng"]
        return latitude, longitude
    else:
        print(f"Geocoding failed: {data['status']}")
        return None, None


# Function to search businesses
def search_businesses(latitude, longitude, radius, characteristics, next_page_token):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type=business&keyword={characteristics}&key={API_KEY}&next_page_token={next_page_token}"
    print("business search url :" + url)
    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK":
        results = data["results"]
        with open("google-json-response_temp.json", "w") as file:
            file.write(json.dumps(data))
            file.write('\n\n')
        # print("results: " + str(results))
        next_page_token = data.get("next_page_token", None)
        # print(next_page_token)
        return results, next_page_token
    else:
        print(f"Places search failed: {data['status']}")
        return [], None


def get_place_details(place_id):
    # url = f"https://places.googleapis.com/v1/places/{place_id}?fields=id,displayName&key={API_KEY}"
    url = f"https://places.googleapis.com/v1/places/{place_id}?fields=addressComponents,currentOpeningHours,displayName,editorialSummary,formattedAddress,googleMapsUri,id,internationalPhoneNumber,location,name,nationalPhoneNumber,priceLevel,primaryType,primaryTypeDisplayName,rating,regularOpeningHours,reviews,shortFormattedAddress,subDestinations,types,userRatingCount,utcOffsetMinutes,websiteUri&key={API_KEY}"
    print("place details url: " + url)

    response = requests.get(url)
    data = response.json()
    print(data)
    # data1['rating'] += 1
    # print(data1)
    return data


# Function to stringify object/array values
def stringify_values(data):
    for key, value in data.items():
        if isinstance(value, dict) or isinstance(value, list):
            data[key] = json.dumps(value)
    return data


# Flatten JSON data
def flatten_json(data1):
    if isinstance(data1, dict):  # Check if data1 is already a dictionary
        return
    data = json.loads(data1)

    flat_data = {}
    for key in keys:
        value = data.get(str(key), "")
        if isinstance(value, dict) or isinstance(value, list):
            value = json.dumps(value)
        flat_data[key] = value
    return flat_data


def saveJSON(data):
    with open("google-json-response.json", "w") as file:
        file.write(json.dumps(data))
        file.write('\n\n')


# Geocode central location
latitude, longitude = geocode_address(central_location)
if not latitude or not longitude:
    exit()

# Loop to retrieve results iteratively
counter = 0
while next_page_token != None:
    if counter == max_loop_count:
        print("token before break: ", next_page_token)
        print(" counter before break", counter)
        break
    print("====================================================================================================================")
    print("COUNTER", counter)
    # print("token at start: ", next_page_token)
    if next_page_token == "initial":
        next_page_token = None
    # print("token after reset to None IF the token is 'initial': ", next_page_token)

    print("======================================================")

    # Call search_businesses to get results and next_page_token
    results, next_page_token = search_businesses(
        latitude, longitude, search_radius, company_characteristics, next_page_token)

    print("token after search_business returns results requested from google api: ", next_page_token)
    # print("results from search_business: ", results)
    # Process retrieved results (append to list, etc.)
    all_results.extend(results)

    # Sleep for X seconds before next request (optional to avoid overwhelming API)
    time.sleep(sleep_time_seconds)

    counter += 1


else:
    print("while loop is done or didn't run  at all")

# Open CSV file for writing
with (open(filename, "w", newline="") as csvfile):
    writer = csv.writer(csvfile)
    writer.writerow(keys)

    for business in all_results:
        details = get_place_details(business['place_id'])
        saveJSON(details)

        flat_data = []
        for key in keys:

            value = ''

            # and 'displayName' in details and 'text' in details['displayName']:
            if key == 'displayName':
                value = str(details['displayName']['text'])
                print("Display Name: " + value)
            elif key == 'utcOffsetMinutes' and 'utcOffsetMinutes' in details:
                value = str(details['utcOffsetMinutes'])
            elif key == 'location':
                if 'location' in details and 'latitude' in details['location']:
                    value = str(details['location']['latitude'])
                if 'location' in details and 'longitude' in details['location']:
                    value += "," + str(details['location']['longitude'])
            elif key == 'types' in details:
                typeslist = ""
                type_cnt = 0
                for type in details['types']:
                    type_cnt += 1
                    if type_cnt < len(details['types']):
                        typeslist += type + "|"
                value = typeslist
            else:
                value = details.get(key, "")

            if isinstance(value, dict) or isinstance(value, list):
                value = json.dumps(value)

            # print(value)

            flat_data.append(value)

        writer.writerow(flat_data)


print("Search results saved to " + filename)
with open(filename, 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
