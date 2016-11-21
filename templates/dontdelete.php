
login_manager = LoginManager()   # LoginManager class is required for login authentication
login_manager.init_app(app)      # application object configured for login
################################################# the user_loader callback

@app.user_loader                 # used to reload the user object from the user ID stored in the session.
                                 #  It takes the unicode ID of a user, and return the corresponding user object.
def load_user(user_id):          # returns None if the object is not valid
    return User.get(user_id)
    
################################################# redirect the user 

@app.route('/secret_page')
@login_required
def secret_page():
  pass
  