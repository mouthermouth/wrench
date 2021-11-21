from flask import Flask 
from flask import render_template

app = Flask(__name__, template_folder = 'HTML')
@app.route("/")
def indexpage():
    return render_template("index.html")

@app.route("/renaissance")
def renaissance():
    return render_template("renaissance.html")

@app.route("/aiera")
def renaisance():
    return render_template("aiera.html")

@app.route("/biotech")
def biotech():
    return render_template("biotech.html")

@app.route("/spacecraze")
def spacecraze():
    return render_template("spacecraze.html")

@app.errorhandler(404)
def errorpage(error):
    return render_template("404.html")

app.run()