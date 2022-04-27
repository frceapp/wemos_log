from threading import Thread
import db, os, datetime, pytz
import time
from flask import Flask, request as rq, render_template, session, redirect, url_for, g
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
global statuson

@app.route("/", methods=['GET', 'POST'])
def login():
    default_data = {
            "gradient": "linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2))",
            "gambar_kucing": "kucing_login.svg",
            "welcome": "welcome.svg"
    }
    if rq.method =='POST':
        headers = rq.headers.get('Host')
        file = open("log_headers.log", "a")
        file.write(str(headers+"\n"))
        session.pop('user', None)
        data_login = db.login(rq.form['username'], rq.form['password'])
        if not data_login:
            default_data['gradient'] = "linear-gradient(180deg, rgba(88,3,173,255) 0%, rgba(34,34,34,255) 100%);"
            default_data['gambar_kucing'] = "kucing_error.svg"
            default_data['welcome'] = "anda.svg"
            return render_template('login.html', data=default_data)
        else:
            session['user'] = rq.form['username']
            return redirect(url_for('table'))
        
            

    return render_template('login.html', data=default_data)

@app.route("/table", methods=['GET', 'POST'])
def table():
    if g.user:
        x, y, z, data_time, a = db.show_time(g.user)[0]
        if rq.method == "POST":
            times = rq.form['time']
            print(len(times))
            if 0 < len(times):
                db.time_set(times, g.user)
                return render_template("table.html", data=db.show_data(g.user), user=g.user, data_time=f"Now time set at {times}")
            else:
                db.time_set(times, g.user)
                return render_template("table.html", data=db.show_data(g.user), user=g.user, data_time=f"Time unset")
        elif rq.method == "GET":
            data = rq.args.get('status')
            if data == "On":
                db.status_set("On", g.user)
                time.sleep(5)
                db.status_set("Off", g.user)
        if len(data_time) == 0:
            endsettime = "Time unset"
        else:
            endsettime = f"Now time set at {data_time}"

        return render_template("table.html", data=db.show_data(g.user), user=g.user, data_time=endsettime)
    return redirect(url_for('login'))


@app.route("/input_data")
def input_data():
    data = rq.args.get('data')
    user = rq.args.get('username')
    x = db.insert_data(data, user)
    return x

@app.route("/status")
def status():
    user = rq.args.get('username')
    x, status = db.show_status(user)
    return f"{status}"

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']
        print(g.user)

@app.route('/end')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('login'))


def runner():
    app.debug = False
    app.run("0.0.0.0", port=8080)

def loop():
    while(True):
        for user in db.show_alluser():
            x, y, z, data_time, a = db.show_time("".join(user))[0]
            now = datetime.now(pytz.timezone("Asia/Jakarta"))
            times = now.strftime("%H:%M:%S")
            if data_time is not None:
                if data_time+":01" == times:
                    print(f"user {''.join(user)}")
                    db.status_set("On", "".join(user))
                    time.sleep(5)
                    db.status_set("Off", "".join(user))
        time.sleep(1)


if __name__ == '__main__':
    server = Thread(target=runner)
    looping = Thread(target=loop)
    server.start()
    looping.start()
