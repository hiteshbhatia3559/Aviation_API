import requests
import json

api_key = "cb357c-3cdad8"

def get_answer(flight_number):
    url = "https://aviation-edge.com/get.php"

    response = json.loads(requests.get(
        url=" http://aviation-edge.com/v2/public/flights?key=" + api_key + "&aircraftIcao=" + flight_number).text)

    return response

while 1:
    input_variable = input("What is your flight number?")
    if input_variable.lower() != "quit":
        found = "NO"
        for i in range(0,10):
            answer = get_answer("B738")
            for item in answer:
                # if input_variable in [item['flight']['iataNumber'],item['flight']['icaoNumber'],item['aircraft']['regNumber']]:
                #     print("YES")
                if input_variable == item['flight']['iataNumber']:
                    found = "YES"
                if input_variable == item['flight']['icaoNumber']:
                    found = "YES"
                if input_variable == item['aircraft']['regNumber']:
                    found = "YES"
        print(found)
    else:
        print("Quitting")
        exit()






