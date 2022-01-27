from cmath import log
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
      user="root",
      password="123",
      database="kelompok4"
    )

mycursor = mydb.cursor()

def show_data():
    mycursor.execute("SELECT * FROM wemos_log ORDER BY id DESC;")
    myresult = mycursor.fetchall()
    return myresult

def insert_data(val, time):
    sql = f"INSERT INTO wemos_log (data, time) VALUES ({val}, {time})"
    mycursor.execute(sql)

    mydb.commit()
    return sql

def login(username, password):
    mycursor.execute(f"SELECT * FROM admin where username='{username}' and password='{password}'")
    myresult = mycursor.fetchall()
    return myresult

print(login("nekomata", "2awfw"))
