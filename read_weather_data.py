from flask import Flask
import pymysql

import requests

OPEN_WEATHER_MAP_API_KEY = "31ddfd85c327437703aecdba29571796"

api_url = "http://api.openweathermap.org/data/2.5/weather?q=Bengaluru&appid=" + OPEN_WEATHER_MAP_API_KEY

app = Flask(__name__)
@app.route('/getBlrWeather')
def get_open_weather_map_data():
  response = requests.get(api_url).json()
  print(response)
  return response

if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
