from flask import Flask, render_template
from db_connect import connection

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template ("index.html")

@app.route('/home')
def home():
    return render_template ("home.html")

@app.route('/other')
def otherpage():
    return render_template ("other.html")

@app.route('/reports')
def reportspage():
    return render_template ("reports.html")

@app.route('/survey')
def survey():
    return render_template ("survey.html")

@app.route('/register')
def register_page():
     try:
    	c, conn=connection()
    	return ("Okay")
     except Exception as e:
        return (str(e))


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5006)

