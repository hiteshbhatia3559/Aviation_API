import requests
import json
import ast

api_key = "cb357c-3cdad8"
not_allowed = ['B37M','B38M','B39M','B3JM','B738']

def get_answer(flight_number):
    url = "https://aviation-edge.com/get.php"

    response = json.loads(requests.get(
        url=" http://aviation-edge.com/v2/public/flights?key=" + api_key + "&flightIata=" + flight_number).text)

    print(response)

# Code outputs the type of aircraft

if __name__ == "__main__":
    while 1:
        flight_number = input("What is your flight number?")
        if flight_number.lower() != "quit":
            get_answer(flight_number)
        else: exit()
