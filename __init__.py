from flask import Flask, render_template, redirect, url_for, request
from db_connect import connection
from DBConnection import DBConnection
import logging
import datetime

app = Flask(__name__)

/* ---------- Open Login Page ------------------*/

@app.route('/')                      
def loginpage():
    return render_template ("index.html")

/* ---------- Open Home Page -------------------*/

@app.route('/home')                  
def home():
    return render_template ("home.html")

/* ---------- Open Other Page ------------------*/

@app.route('/other/')                
def otherpage():
   return render_template ("other.html")


/* ----------- Open Results Page ---------------*/

@app.route('/result/', methods=['POST', 'GET']) 
def result():

   if request.method == 'POST':
      #result = request.form
     try:
        types = request.form['type_data']
        finances = request.form['finance_data']
        attendances = request.form['attendance_data']
        rates = request.form['rate_data']
        c, conn = connection()
        c.execute("INSERT INTO event(type, finance, attendance, response_rate) VALUES (%s, %s, %s, %s)",(types,finances,attendances,rates) )
        con.commit()
        msg = "Data successfully added"
     except:
         con.rollback()
         msg = "error in insert operation"
     finally:
         return render_template("result.html", msg = msg)
         con.close()

      

@app.route('/reports')
def reportspage():
    return render_template ("reports.html")

/* ------------ Open Survey Page ---------------*/

@app.route('/survey')
def survey():
    return render_template ("survey.html")


@app.route('/register')
def register_page():
     try:
    	c, conn=connection()
     except Exception as e:
        return (str(e))

/* -----Build the reports for the reports page ----*/

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
  
  rawdata = conn.query("SELECT * FROM event")
  
  attendance_dic_data = {'Speaker': 0, 'Panel':0, 'Training':0, 'Forum':0, 'Festival':0, 'Other':0}
  finance_dic_data = {'Speaker': 0, 'Panel':0, 'Training':0, 'Forum':0, 'Festival':0, 'Other':0}
  other_dic_data = {'Speaker': 0, 'Panel':0, 'Training':0, 'Forum':0, 'Festival':0, 'Other':0}
  
  if report_selection == "attendance":
  	for item in rawdata:
  		attendance_dic_data[item['type']] += item['attendance']
  elif report_selection == "finance":
  	for item in rawdata:
  		finance_dic_data[item['type']] += item['finance']
  else:
  	for item in rawdata:
  		other_dic_data[item['type']] += item['other']
  	
  del conn  
  
  return render_template("currentreport.html", selection = report_selection, adata = attendance_dic_data, fdata = finance_dic_data, odata = other_dic_data)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5006)
