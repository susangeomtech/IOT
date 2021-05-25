
from flask import Flask
import pymysql
import requests

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

  for value in currentWeather:
    weather_data = {
      'clouds': currentWeather["clouds"],
      'dew_point': currentWeather["dew_point"],
      'dt':currentWeather["dt"],
      'feels_like': currentWeather["feels_like"],
      'humidity': currentWeather["humidity"],
      'temp': currentWeather["temp"]
      }

  for value in weatherReport:
    weather_report_data = {
      'id': weatherReport["id"],
      'description': weatherReport["description"],
      'icon': weatherReport["icon"],
      'main': weatherReport["main"]
      }


  conn = pymysql.connect(database="weatherdata",user="susan",password="hello1234",host="localhost")
  cur = conn.cursor()
    
  insert_weather_data = "INSERT INTO currentWeatherTable(clouds, dew_point, dt, feels_like, humidity, temp ) VALUES (%(clouds)s, %(dew_point)s, %(dt)s, %(feels_like)s, %(humidity)s, %(temp)s)"
  cur.execute(insert_weather_data, weather_data)

  insert_weather_report_data = "INSERT INTO weatherSummaryTable (id, description, icon, main) VALUES (%(id)s, %(description)s, %(icon)s, %(main)s)"
  cur.execute(insert_weather_report_data, weather_report_data)
  conn.commit()

  return "Success"
 
if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
