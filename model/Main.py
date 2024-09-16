import requests
import json


def get_weather():
   # API key and base URL
   api_key = "954d1ec6aadb45e58c3221701241509"

   # Get user input for city and date
   location = input("City Name: ")
   # date = input("Date (yyyy-MM-dd): ")

   # API endpoint
   # need to pay for this one
   # endpoint = f"http://api.weatherapi.com/v1/future.json?key={api_key}&q={location}&dt={date}"
   endpoint2 = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"


   try:
       # Make the API request
       response = requests.get(endpoint2)
       if response.status_code == 200:
           response_data = response.json()
           # Extract the current temperature in Fahrenheit
           temp_f = response_data['current']['temp_f']
           print(f"Current temperature in {location}: {temp_f}°F")
       else:
           print(f"Failed to retrieve data: {response.status_code}")
   except Exception as e:
       print(f"Error occurred: {e}")

   # find the min and max temp of specific place on a specific date.
   # need to pay for this one
   # try:
   #     # Make the API request
   #     response = requests.get(endpoint)
   #
   #     if response.status_code == 200:
   #         response_data = response.json()
   #
   #         # Extract min and max temperatures
   #         min_temp_f = response_data['forecast']['forecastday'][0]['day']['mintemp_f']
   #         max_temp_f = response_data['forecast']['forecastday'][0]['day']['maxtemp_f']
   #
   #         # Print the minimum and maximum temperatures
   #         print("-----------------------------------------------------------")
   #         print(f"{location}'s weather on {date} is between {min_temp_f}°F and {max_temp_f}°F")
   #         print("-----------------------------------------------------------")
   #         print()
   #         print("***********************************************************")
   #         print(f"Detailed View: ")
   #         print(f"Minimum Temperature: {min_temp_f}°F")
   #         print(f"Maximum Temperature: {max_temp_f}°F")
   #         print("***********************************************************")
   #     else:
   #         print(
   #             f"Request failed: {response.status_code} - {response.json().get('error', {}).get('message', 'Unknown error')}")
   # except requests.exceptions.RequestException as e:
   #     print(f"An error occurred: {e}")



# if __name__ == "__main__":
#    get_weather()

get_weather()