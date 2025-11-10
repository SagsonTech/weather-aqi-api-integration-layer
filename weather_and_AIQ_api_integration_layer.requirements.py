# =============================================
# Python Exercise: Weather & AQI Integration
# =============================================

# 1. Create a class WeatherClient:
#    - Method: get_weather(city)
#    - Makes a GET request to a weather API
#    - Add timeout=5 seconds
#    - Add retry logic: 3 retries with exponential backoff
#    - Validate success using status_code == 200
#    - Parse JSON and return: temperature, humidity

# 2. Create a class AQIClient:
#    - Method: get_aqi(city)
#    - Calls an air quality API
#    - Handles HTTP errors (4xx, 5xx)
#    - If rate limited (429), wait 1 second and retry
#    - Return AQI, PM2_5, PM10

# 3. Create a class DataAggregator:
#    - Method: get_city_report(city)
#    - Calls both clients
#    - Combines data into a single dict:
#        {
#          "city": city,
#          "temperature": ...,
#          "humidity": ...,
#          "aqi": ...,
#          "pm2_5": ...,
#          "pm10": ...
#        }

# 4. Persistence Layer (SQLite):
#    - Create a table city_reports
#    - Columns:
#        id INTEGER PRIMARY KEY,
#        city TEXT,
#        temperature REAL,
#        humidity REAL,
#        aqi INTEGER,
#        pm2_5 REAL,
#        pm10 REAL,
#        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#
#    - Function save_report(data_dict)

# 5. CLI command (Python script)
#    - Usage:
#        python fetch_report.py "New York"
#
#    - Fetches + Saves + Prints:
#        "Report saved for New York at 2025-11-10 22:00"
