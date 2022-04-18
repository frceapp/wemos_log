import datetime, pytz
import mysql.connector

from datetime import datetime

mydb = mysql.connector.connect(
	  host="localhost",
      user="root",
      password="123",
      database="aplikasi_db"
    )

mycursor = mydb.cursor()

def show_data(user):
    mycursor.execute(f"SELECT * FROM wemos_log WHERE username='{user}' ORDER BY id DESC;")
    myresult = mycursor.fetchall()
    return myresult

def insert_data(val, username):
    now = datetime.now(pytz.timezone("Asia/Jakarta"))
    time = now.strftime("%H:%M")
    tanggal = now.strftime("%d %B %Y")
    sql = f'INSERT INTO wemos_log (data, time, tanggal, username) VALUES ({val}, "{time}", "{tanggal}", {username})'
    mycursor.execute(sql)

    mydb.commit()
    return sql

def login(username, password):
    mycursor.execute(f"SELECT * FROM admin where username='{username}' and password='{password}'")
    myresult = mycursor.fetchall()
    return myresult
