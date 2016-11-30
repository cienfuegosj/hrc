from flask import Flask, render_template, redirect, url_for, request
from db_connect import connection
from DBConnection import DBConnection
import logging
import datetime

app = Flask(__name__)

@app.route('/')                      
def loginpage():
    '''this function displays the loginpage'''
    return render_template ("index.html")



@app.route('/home')                  
def home():
    '''this function displays the home page'''
    return render_template ("home.html")



@app.route('/other/')                
def otherpage():
   '''this function displays the other details page'''
   return render_template ("other.html")




@app.route('/result/', methods=['POST', 'GET']) 
def result():
   '''this function handles the post method and sends the values to the database'''

   if request.method == 'POST':       # Checks if the method is a post method
      #result = request.form
     try:
        types = request.form['type_data']       # gets the event type value
        finances = request.form['finance_data']    # gets the value of the finances
        attendances = request.form['attendance_data']   # gets the attendance value
        rates = request.form['rate_data']          # gets the rates value
        c, conn = connection()        # connects to the database
        c.execute("INSERT INTO event(type, finance, attendance, response_rate) VALUES (%s, %s, %s, %s)",(types,finances,attendances,rates) ) #gets the query
        conn.commit()     # inserts the query into the database
        msg = "Data successfully added"  # gets a successful message
        c.close()     # closes the connection 
        conn.close()    # closes the final connnection 

     except:
         msg = "error in insert operation"       # gets message if the connection fails
     
     return render_template("result.html", msg = msg)
   
   return "Ok"
       

      

@app.route('/reports')
def reportspage():
    '''this function displays the reports page'''
    return render_template ("reports.html")



@app.route('/survey')
def survey():
    '''this function displays the survey page'''
    return render_template ("survey.html")


@app.route('/register')
def register_page():
     '''this is a test function'''
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
