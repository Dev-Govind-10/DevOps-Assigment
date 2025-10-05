from flask import Flask, render_template, flash, redirect, url_for
from datetime import datetime
from flask import request
import requests

app = Flask(__name__)

BACKEND_URL = "http://0.0.0.0:9000"

@app.route('/')
def home():
    day = datetime.today().strftime('%A')
    time = datetime.today().strftime('%H:%M:%S')
    return render_template('index.html', day_of_the_week=day, time=time)

@app.route('/submit', methods=['POST'])
def submit():
    # form_data = dict(request.form)
    # requests.post(BACKEND_URL + "/submit", json=form_data)
    # return "data submited successfully"
    form_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"]
    }

    try:
        response = requests.post(BACKEND_URL + "/submit", json=form_data)
        if response.status_code == 200:
            return redirect(url_for("success"))
        else:
            flash(f"Error: {response.json().get('error', 'Unknown error')}")
            return redirect(url_for("index"))
    except Exception as e:
        flash(f"Error connecting to backend: {str(e)}")
        return redirect(url_for("index"))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
