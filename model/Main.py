import requests
import json


def get_weather():
   # Input your working API key
   api_key = ""

   # Get user input for city and date
   location = input("City Name: ")
   date = input("Date (yyyy-MM-dd): ")

   # API endpoint for future weather data
   # Note: Requires a paid plan for future data access
   endpoint = f"http://api.weatherapi.com/v1/future.json?key={api_key}&q={location}&dt={date}"

   try:
       # Make the API request
       response = requests.get(endpoint)

       if response.status_code == 200:
           response_data = response.json()

           # Extract min and max temperatures
           min_temp_f = response_data['forecast']['forecastday'][0]['day']['mintemp_f']
           max_temp_f = response_data['forecast']['forecastday'][0]['day']['maxtemp_f']

           # Print the temperature details
           print("-----------------------------------------------------------")
           print(f"{location}'s weather on {date} is between {min_temp_f}°F and {max_temp_f}°F")
           print("-----------------------------------------------------------")
           print()
           print("***********************************************************")
           print(f"Detailed View: ")
           print(f"Minimum Temperature: {min_temp_f}°F")
           print(f"Maximum Temperature: {max_temp_f}°F")
           print("***********************************************************")
       else:
           print(
               f"Request failed: {response.status_code} - {response.json().get('error', {}).get('message', 'Unknown error')}")
   except requests.exceptions.RequestException as e:
       print(f"An error occurred: {e}")



if __name__ == "__main__":
   get_weather()
