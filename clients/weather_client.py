import requests
from requests.adapters import HTTPAdapter, Retry

class InvalidCityException(Exception):
    pass

class APIException(Exception):
    pass

class WeatherClient:
    __weather_uri = "https://api.open-meteo.com/v1/forecast?"
    __lat_long_uri = "https://geocoding-api.open-meteo.com/v1/search?"
    __session = requests.Session()
    __retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
    __session.mount("https://", HTTPAdapter(max_retries=__retries))
    
    def get_weather(self, city):
        if len(city) == 0:
            raise InvalidCityException("Invalid city passed to the weather client")
        
        try:
            lat_lon_response = self.__get_lat_lon(city)
            lat_lon_json_response = lat_lon_response.json()

            if "results" not in lat_lon_json_response.keys():
                raise InvalidCityException("Unable to find the city coordinates. Make sure the city name is valid or if the location exists")
            
            latitude = lat_lon_json_response.get('results')[0].get('latitude')
            longitude = lat_lon_json_response.get('results')[0].get('longitude')

            weather_response = self.__session.get(f"{self.__weather_uri}latitude={latitude}&longitude={longitude}&current_weather=true", timeout=5.000)
            
            if weather_response.status_code != 200:
                raise APIException(f"Request failed with status code {weather_response.status_code}")
            
            weather_json_response = weather_response.json()
            return {'temperature': weather_json_response.get("current_weather").get("temperature"), 'windspeed': weather_json_response.get("current_weather").get("windspeed")}

            
        except Exception as e:
            print("Error:", e)
    
    def __get_lat_lon(self, city):
        try:
            response = self.__session.get(f"{self.__lat_long_uri}name={city}", timeout=5.000)
            return response
        except requests.exceptions.Timeout as e:
            print("Request timed out")
        
