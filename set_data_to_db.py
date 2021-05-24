
from flask import Flask
import pymysql
import requests
import pymysql


OPEN_WEATHER_MAP_API_KEY = "31ddfd85c327437703aecdba29571796"
api_url = "http://api.openweathermap.org/data/2.5/weather?q=Bengaluru&appid=" + OPEN_WEATHER_MAP_API_KEY

app = Flask(__name__)
@app.route("/")
def welcome():
  return "Welcome to Amrita Intelligent Infrastructure Data Management and Control Panel App. \n Use one of the options below."

@app.route('/hello')
def  hello():
  return "Hello"

@app.route('/getWeatherData')
def get_open_weather_map_data():
  response = requests.get(api_url).json()
  print(response)
  return response

@app.route('/setWeatherDataToDb')
def set_db_data():
  response = get_open_weather_map_data()
  print(response)
  currentWeather = response['current']
  weatherReport = currentWeather['weather'][0]
  conn = pymysql.connect(database="WeatherDB",user="admin",password="admin",host="localhost")
  cur = conn.cursor()
  sql_query = "INSERT INTO currentWeatherTable (clouds, dt, feels_like, humidity, temp ) VALUES (%(clouds)s,  %(dt)s, %(feels_like)s, %(humidity)s, %(temp)s )"
  cur.execute(sql_query, currentWeather)
  sql_query = "INSERT INTO weatherSummaryTable (id, description, icon, main) VALUES (%(id)s, %(description)s, %(icon)s, %(main)s)"
  cur.execute(sql_query, weatherReport)
  
  return currentWeather
  return response

if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
