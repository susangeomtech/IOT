import pymysql

conn =pymysql.connect(database="ab1",user="sai",password="sai",host="localhost")
cur=conn.cursor()

#create database
cur.execute("CREATE TABLE users(id int primary, name text, age int, gender text, address text);")

#to store user data

name = "user1"
age = 25
gender = "M"
address = "Tamilnadu"

data={'name':name,'age':age,'gender':gender,'address':address}
print(data)

# Saving data to DB
cur.execute("INSERT INTO users (name,age,gender,address) VALUES (%(name)s,%(age)s,%(gender)s,%(address)s);",data)
conn.commit()
print("saved to db")

#reading data from DB
cur.execute("SELECT * FROM users;")
#get one row
data1=cur.fetchone()
#get all rows
data2=cur.fetchall()

print(data1)
print(data2)
