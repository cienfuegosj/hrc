from flask import Flask, render_template, redirect, url_for, make_response, send_file, request, Response, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from db_connect import connection
from DBConnection import DBConnection
import logging
import datetime
import copy
import time


app = Flask(__name__)

app.config.update(
	SECRET_KEY = 'BHRC'
)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "loginpage"



class User(UserMixin):
	def __init__(self, id, name="mharrington", password="harrington12qwaszx!"):
		self.id = id
		self.name = name
		self.password = password

	def __repr__(self):
		return "%d/%s/%s" % (self.id, self.name, self.password)


# Login Page
@app.route('/login', methods=['POST'])
def login():

	if request.method == "POST":
		username = request.form['username']
		password = request.form['pwd']
		conn = DBConnection()
		users = conn.query("SELECT * FROM users WHERE username = '{0}' AND password = '{1}';".format(username, password))

		del conn

		if len(users) == 1:
			user = User(users[0]['UID'], users[0]['username'], users[0]['password'])
			login_user(user)
			return redirect(url_for("home"))
		else:
			return abort(401)
	else:
		return redirect(url_for("loginpage"))

# Log out and return to the index page
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("loginpage"))


# Handle login 
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
    
    
# Callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

@app.route('/')                      
def loginpage():
    '''this function displays the loginpage'''
    return render_template ("index.html")


@app.route('/home')
@login_required
def home():
    '''this function displays the home page'''
    return render_template ("home.html")



@app.route('/other/')
@login_required
def otherpage():
   '''this function displays the other details page'''
   return render_template ("other.html")


@app.route('/result/', methods=['POST', 'GET'])
@login_required
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
         msg = "Error in Insert Operation."       # gets message if the connection fails
     
     return render_template("result.html", msg = msg)
   
   return "Ok"
      


@app.route('/reports')
@login_required
def reportspage():
    '''this function displays the reports page'''
    return render_template ("reports.html")



@app.route('/survey/')
@login_required
def survey():
    '''this function displays the survey page'''
    return render_template ("survey.html")


@app.route('/result2/', methods=['POST', 'GET'])
@login_required
def result2():
   '''this function handles the post method and sends the values to the database'''

   if request.method == 'POST':       # Checks if the method is a post method
     #check = request.form
     try:
     	titles = request.form['title_data']       # gets the title value
     	dates = request.form['date_data']    # gets the value of the date
     	locations= request.form['location_data']       # gets the location value
     	type2 =request.form['types_data']    # gets the value of the event type
     	govts=request.form['govt_data']
     	#residents=request.form['residency_data']   #gets the value of the residency
     	residents = request.form.get('residency_data', None)
     	if residents is None:
        	residents="None"
     	races=request.form.get('race_data', None)    # gets the race value
     	if races is None:
        	races="None"
     	sexes=request.form.get('sex_data', None)
     	if sexes is None:
        	sexes="None"
     	ages=request.form.get('age_data', None)
     	if ages is None:
        	ages="None" 
       	########## the lines below gets the values of the questions from numbers 1-17
     	one=request.form['q1']
     	two=request.form['q2']
     	a3=request.form['q3']
     	a4=request.form['q4']
     	a5=request.form['q5']
     	a6=request.form['q6']
     	a7=request.form['q7']
     	a8=request.form['q8']
     	a9=request.form['q9']
     	a10=request.form.get('q10_data', None)
     	if a10 is None:
        	a10="None"
     	a11=request.form.get('q11_data', None)
     	if a11 is None:
        	a11="None"
     	a12=request.form['q12']
     	a13=request.form['q13']
     	a14=request.form['q14']
     	a15=request.form['q15']
     	a16=request.form['q16']
     	a17=request.form.get('q17_data', None)
     	if a17 is None:
        	a17="None"
     	c, conn = connection()        # connects to the database
     	c.execute("INSERT INTO survey(location, eventype, title, date, residency, race, sex, age, govt, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(locations, type2, titles, dates, residents, races, sexes, ages, govts, one, two, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17) ) #gets the query
     	conn.commit()     # inserts the query into the database
     	msg = "Data successfully added"  # gets a successful message
     	c.close()     # closes the connection
     	conn.close()    # closes the final connnection

     except:
      	msg = "Insert operation failed. Ensure you fill out all the required information in the survey next time."       # gets message if the connection fails

     return render_template("result2.html", msg=msg)
     #return render_template("result2.html", check=check)
   return "Ok"



@app.route('/register')
@login_required
def register_page():
     '''This is a test function'''
     try:
    	c, conn=connection()
     except Exception as e:
        return (str(e))



@app.route('/report/<report_selection>', methods = ['GET'])
@login_required
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
  
  raweventdata = conn.query("SELECT * FROM event") 
  attendance_dic_data = {'Speaker': 0, 'Panel':0, 'Training':0, 'Forum':0, 'Festival':0, 'Other':0}
  finance_dic_data = {'Speaker': 0, 'Panel':0, 'Training':0, 'Forum':0, 'Festival':0, 'Other':0}
  

  rawsurveydata = conn.query("SELECT * FROM survey")
  qdo = {'N/A': 0, 'Strongly Disagree': 0, 'Disagree': 0, 'No opinion': 0,
  						'Agree': 0, 'Strongly Agree': 0
  						}
  questions_dic_data = {'q1': copy.deepcopy(qdo), 'q2': copy.deepcopy(qdo), 'q3': copy.deepcopy(qdo),
  					 	'q4': copy.deepcopy(qdo), 'q5': copy.deepcopy(qdo), 'q6': copy.deepcopy(qdo),
  					 	'q7': copy.deepcopy(qdo), 'q8': copy.deepcopy(qdo), 'q9': copy.deepcopy(qdo),
  					 	'q12': copy.deepcopy(qdo), 'q13': copy.deepcopy(qdo), 'q14': copy.deepcopy(qdo),
  					 	'q15': copy.deepcopy(qdo)
  						}
  
  if report_selection == "attendance":
  	for item in raweventdata:
  		attendance_dic_data[item['type']] += item['attendance']
  elif report_selection == "finance":
  	for item in raweventdata:
  		finance_dic_data[item['type']] += item['finance']
  elif report_selection=="survey":
  	for i in range(1,10):
  		for item in rawsurveydata:
  			if item['q' + str(i)] == 'N/A':
				questions_dic_data['q' + str(i)]['N/A'] += 1
			elif item['q' + str(i)] == 'Strongly Disagree':
				questions_dic_data['q' + str(i)]['Strongly Disagree'] += 1
			elif item['q' + str(i)] == 'Disagree':
				questions_dic_data['q' + str(i)]['Disagree'] += 1
			elif item['q' + str(i)] == 'No opinion':
				questions_dic_data['q' + str(i)]['No opinion'] += 1
			elif item['q' + str(i)] == 'Agree':
				questions_dic_data['q' + str(i)]['Agree'] += 1
			elif item['q' + str(i)] == 'Strongly Agree':
				questions_dic_data['q' + str(i)]['Strongly Agree'] += 1
	for i in range(12, 16):
  		for item in rawsurveydata:
  			if item['q' + str(i)] == 'N/A':
				questions_dic_data['q' + str(i)]['N/A'] += 1
			elif item['q' + str(i)] == 'Strongly Disagree':
				questions_dic_data['q' + str(i)]['Strongly Disagree'] += 1
			elif item['q' + str(i)] == 'Disagree':
				questions_dic_data['q' + str(i)]['Disagree'] += 1
			elif item['q' + str(i)] == 'No opinion':
				questions_dic_data['q' + str(i)]['No opinion'] += 1
			elif item['q' + str(i)] == 'Agree':
				questions_dic_data['q' + str(i)]['Agree'] += 1
			elif item['q' + str(i)] == 'Strongly Agree':
				questions_dic_data['q' + str(i)]['Strongly Agree'] += 1
	
  del conn
  
  if report_selection == "attendance" or report_selection == "finance" or report_selection == "survey":
  
  	return render_template("generatereport.html", selection = report_selection,
  						 	adata = attendance_dic_data, fdata = finance_dic_data,
  						 	qdata = questions_dic_data)
  						 	
  elif report_selection == "rawsurvey":
  
  	return render_template("rawsurveys.html", surveys=rawsurveydata)
  	
@app.route('/survey/<SID>', methods=['GET'])
@login_required
def SpecificSurvey(SID):

	#Connect to the database
	try:
		conn = DBConnection()
		logging.info("Database Connection Success \t" + str(datetime.date.today()))
	except Exception as e:
		logging.info("Database Connection Failed \t" + str(datetime.date.today()))
    	
	surveys = conn.query("SELECT * FROM survey WHERE SID = '" + str(SID) + "'") 
	survey = surveys[0]	
	return render_template("specificsurvey.html", survey=survey)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
