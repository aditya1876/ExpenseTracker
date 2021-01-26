from flask import Flask
app = Flask(__name__)

#Home Page
@app.route('/')
def homePage():
    return 'Hello World1'

#Username Page
@app.route('/<username>')
def userPage(username):
    return 'Hi %s !' %username

#Consolidated Page
@app.route('/<username>/consolidated')
def consolidatedPage(username):
    return 'consolidated page for %s' %username

#Report Page
@app.route('/<username>/report')
def reportPage(username):
    return 'report page for %s' %username

if __name__ == '__main__':
    app.run(debug = True)