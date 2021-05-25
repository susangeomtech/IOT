
from flask import Flask
import pymysql
import requests
import pymysql

lat = '13.02'
lon = '77.68'
OPEN_WEATHER_MAP_API_KEY = "31ddfd85c327437703aecdba29571796"
#Create openweathermap url
api_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&exclude=hourly,daily,minutely,alerts+&appid="+OPEN_WEATHER_MAP_API_KEY+"&units=metric"

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
  conn = pymysql.connect(database="weatherdata",user="susan",password="hello1234",host="localhost")
  cur = conn.cursor()
  print(currentWeather)
  cur.execute("INSERT INTO currentWeatherTable (clouds, dew_point, dt, feels_like, humidity, temp ) VALUES (%(clouds)s,  (%dew_point)s, %(dt)s, %(feels_like)s, %(humidity)s, %(temp)s )", currentWeather)
  cur.execute("INSERT INTO weatherSummaryTable (id, description, icon, main) VALUES (%(id)s, %(description)s, %(icon)s, %(main)s)", weatherReport)
  return currentWeather
 
if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
