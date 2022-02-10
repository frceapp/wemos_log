import db, os, socket
from flask import Flask, request as rq, render_template, session, redirect, url_for, g

app = Flask(__name__)
app.secret_key = os.urandom(24)
host = socket.gethostbyname(socket.gethostname())

@app.route("/", methods=['GET', 'POST'])
def login():
    if rq.method =='POST':
        headers = rq.headers.get('Host')
        file = open("log_headers.log", "a")
        file.write(str(headers+"\n"))
        session.pop('user', None)
        data_login = db.login(rq.form['username'], rq.form['password'])
        if not data_login:
            wrong = "login_salah.jpg"
            return render_template('login.html', data=wrong)

        user, password, role = data_login[0]
        if rq.form['username'] == user and rq.form['password'] == password:
            session['user'] = rq.form['username']
            return redirect(url_for('table'))
        else:
            wrong = "login_salah.jpg"
            return render_template('login.html', data=wrong)
        
            

    return render_template('login.html', data="bg.jpg")

@app.route("/table")
def table():
    if g.user:
        end_sesion = url_for('dropsession')
        return render_template("table.html", data=db.show_data(), host=host, name=g.user, end_sesion=end_sesion)
    return redirect(url_for('login'))


@app.route("/input_data")
def input_data():
    data = rq.args.get('data')
    time = rq.args.get('time')
    x = db.insert_data(data, time)
    return x

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']

@app.route('/end')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=8080)
