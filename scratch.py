import requests
import json

api_key = "cb357c-3cdad8"

def get_answer(flight_number):
    global api_key
    response = json.loads(requests.get(
        url=" http://aviation-edge.com/v2/public/flights?key=" + api_key + "&aircraftIcao=" + flight_number).text)

    return response

print(get_answer("B737-900"))