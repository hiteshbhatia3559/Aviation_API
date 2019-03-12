import requests
import json
import ast

api_key = 'cb357c-3cdad8'
flight_number = "6E263"
url = "https://aviation-edge.com/get.php"

response = json.loads(requests.get(url=" http://aviation-edge.com/v2/public/flights?key=cb357c-3cdad8&flightIata=6E263").text)

print(response[0]['aircraft']['icaoCode'])