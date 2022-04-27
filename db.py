import datetime, pytz
from multiprocessing.spawn import prepare
import mysql.connector

from datetime import datetime
def db():
    return mysql.connector.connect(
	  host="localhost",
      user="root",
      password="123",
      database="aplikasi_db"
    )


def show_data(user):
    mydb = db()
    mycursor = mydb.cursor(prepared=True,)
    mycursor.execute(f"SELECT * FROM wemos_log WHERE username=%s ORDER BY id DESC;", (user,))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

def insert_data(val, username):
    mydb = db()
    mycursor = mydb.cursor(prepared=True,)
    now = datetime.now(pytz.timezone("Asia/Jakarta"))
    time = now.strftime("%H:%M")
    tanggal = now.strftime("%d %B %Y")
    sql = f'INSERT INTO wemos_log (data, time, tanggal, username) VALUES (%s, %s, %s, %s)'
    mycursor.execute(sql, (val, f"{time}", f"{tanggal}", username,))
    mycursor.close()

    mydb.commit()
    return sql

def login(username, password):
    mydb = db()
    mycursor = mydb.cursor(prepared=True,)
    mycursor.execute(f"SELECT * FROM admin where username=%s and password=%s", (username, password))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

def time_set(val, username):
    mydb = db()
    mycursor = mydb.cursor(prepared=True,)

    sql = f'UPDATE admin SET time=%s WHERE username=%s'
    mycursor.execute(sql, (val, username,))
    mycursor.close()

    mydb.commit()
    return sql

def show_time(user):
    mydb = db()
    mycursor = mydb.cursor(prepared=True,)
    mycursor.execute(f"SELECT * FROM admin WHERE username=%s;", (user,))
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

def status_set(val, username):
    mydb = db()
    mycursor = mydb.cursor(prepared=True,)

    sql = f'UPDATE admin SET status=%s WHERE username=%s'
    mycursor.execute(sql, (val, username,))
    mycursor.close()

    mydb.commit()
    return sql

def show_status(user):
    mydb = db()
    mycursor = mydb.cursor(prepared=True,)
    mycursor.execute(f"SELECT username, status FROM admin WHERE username=%s;", (user,))
    myresult = mycursor.fetchall()[0]
    mycursor.close()
    return myresult

def show_alluser():
    mydb = db()
    mycursor = mydb.cursor(prepared=True,)
    mycursor.execute(f"SELECT username FROM admin")
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult
