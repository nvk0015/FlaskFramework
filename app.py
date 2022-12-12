from flask import Flask

##intitializing the flask with an object called "app", which acts as WSGI application
app = Flask(__name__)

#decorator binded with a function
@app.route(rule='/')
def welcome():
    return 'Welcome to FLASK, the first test for a web application, using debug parameter while running the app'

#decorator binded with a function
@app.route(rule='/members')
def welcomeMembers(rule='/members'):
    return 'Welcome all the menmbers'
    
if __name__=='__main__':
    app.run(debug=True)