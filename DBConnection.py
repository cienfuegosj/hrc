import MySQLdb

class DBConnection:
  '''
  A database Application Programming Interface that simplies the use of the MySQLdb
  class in order to connect, send, and disconnect from the database
  '''
  ###### Database Credentials #####
  host = 'localhost'
  user = 'hrc'
  password = 'harrington12qwaszx!'
  db = 'hrc'
  #################################
    
  def __init__(self):
    self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
    self.cursor = self.connection.cursor()

  def insert(self, query):
    try:
      self.cursor.execute(query)
      self.connection.commit()
    except:
      self.connection.rollback()


  def query(self, query):
    cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
    cursor.execute(query)

    return cursor.fetchall()

  def __del__(self):
    self.connection.close()
