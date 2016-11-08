from db_connect import connection

def BuildReport(selection):
  '''
    Builds a report by querying the database and asking for the selected information.
    We also build a list to then render the report_modal.html template.
    param: selection is of type string so we can use it to query to the database.
  '''
  
  #Connect to the database
  #Query the database and extract data in a form of a container datatype
  #render the template 'report_modal.html' with the list parameter.
  #Use Jinja in report_modal.html to display information
  
  