# =============================================
# Python Exercise: Weather Integration
# =============================================

# 1. Create a class WeatherClient:
#    - Method: get_weather(city)
#    - Makes a GET request to a weather API
#    - Add timeout=5 seconds
#    - Add retry logic: 3 retries with exponential backoff
#    - Validate success using status_code == 200
#    - Parse JSON and return: temperature, humidity

# 2. Persistence Layer (SQLite):
#    - Create a table city_reports
#    - Columns:
#        id INTEGER PRIMARY KEY,
#        city TEXT,
#        temperature REAL,
#        windspeed REAL,
#        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#
#    - Function save_report(data_dict)

# 3. CLI command (Python script)
#    - Usage:
#        python fetch_report.py "New York"
#
#    - Fetches + Saves + Prints:
#        "Report saved for New York at 2025-11-10 22:00"
