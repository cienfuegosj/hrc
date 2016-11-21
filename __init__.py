from flask import Flask, render_template, redirect, url_for, request
from db_connect import connection
from DBConnection import DBConnection
import logging
import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template ("index.html")

@app.route('/home')
def home():
    return render_template ("home.html")


@app.route('/other/')
def otherpage():

   return render_template ("other.html")



@app.route('/result/', methods=['POST', 'GET'])
def result():
   
   if request.method == 'POST':
      #result = request.form
      types = request.form['type_data']
      finances = request.form['finance_data']
      attendances = request.form['attendance_data']
      rates = request.form['rate_data']
      return render_template("result.html",result = )
   
   return 'OK'





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
     except Exception as e:
        return (str(e))


      
@app.route('/report/<report_selection>', methods = ['GET'])
def BuildReport(report_selection):

  '''
    Builds a report by querying the database and asking for the selected information.
    We also build a list to then render the report_modal.html template.
    param: selection is of type string so we can use it to query to the database.
  '''
  
  logging.basicConfig(filename='Report.log',level=logging.DEBUG)
  
  #Connect to the database
  
  try:
    conn = DBConnection()
    logging.info("Database Connection Success \t" + str(datetime.date.today()))
  except Exception as e:
    logging.info("Database Connection Failed \t" + str(datetime.date.today()))
    
  # Query the database and extract data in a form of a container datatype
  
  data = conn.query("SELECT * FROM event")
  
  del conn  
    
  return render_template("currentreport.html", selection = report_selection, data = data)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5006)

