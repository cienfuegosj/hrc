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
     except Exception as e:
        return (str(e))
        
@app.route('/report/<report_selection>')
def BuildReport(report_selection):

  '''
    Builds a report by querying the database and asking for the selected information.
    We also build a list to then render the report_modal.html template.
    param: selection is of type string so we can use it to query to the database.
  '''
  
  #Connect to the database
  try:
    c, conn = connection()
  except Exception as e:
    return str(e)
    
  #Query the database and extract data in a form of a container datatype
  
  
  #render the template 'report_modal.html' with the list parameter.
  
  
  #Use Jinja in report_modal.html to display informationls
  
@app.route('/reportinformation')
def ReportInfo(data):
  return render_template ("report_modal.html", data)
  

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5006)

