from flask import Flask
import pymysql
import requests
import pymysql

app = Flask(__name__)
@app.route("/")
def welcome():
  return "Welcome to Amrita Intelligent Infrastructure Data Management and Control Panel App. \n Use one of the options below."

@app.route('/hello')
def  hello():
  return "Hello"


@app.route('/setWeatherDataToDb')
def set_db_data():
  conn = pymysql.connect(database="WeatherDB",user="admin",password="admin",host="localhost")
  cur = conn.cursor()
  sql_query = "CREATE TABLE currentWeatherTable(id int auto_increment primary key, clouds text, dew_point text, dt text, feels_like text, humidity text, temp text)  
  cur.execute(sql_query)
  sql_query = "CREATE TABLE weatherSummaryTable(id int auto_increment primary key, description text, icon text, main text)
  cur.execute(sql_query)
  sql_query = "show tables"
  retval = cur.execute(sql_query)
  return retval

if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
