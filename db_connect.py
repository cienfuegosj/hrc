import MySQLdb

def connection():
  '''Connects to the database
  params: host is a string variable and since the databse in the tango.berea.edu and the web application is in the
  same server, we refer to itself, which explains the 'localhost'. 
  
          user is a string that contains the name of the user; in our case, it is 'hrc'
          passwd is a string that contains the password of the database.
          db is a string variable that contains the database name
  '''
  
  conn = MySQLdb.connect(host = "localhost", user = "hrc", passwd = "harrington12qwaszx!", db = "hrc")
  c = conn.cursor()
  return c, conn
