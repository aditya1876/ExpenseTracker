from flask import Flask, render_template
app = Flask(__name__)

#Home Page
@app.route('/')
def homePage():
    return render_template('index.html')

#Username Page
@app.route('/<username>')
def userPage(username):
    return render_template('Username.html', username=username)

#Consolidated Page
@app.route('/<username>/consolidated')
def consolidatedPage(username):
    return render_template('Consolidated.html', username=username)

#Report Page
@app.route('/<username>/report')
def reportPage(username):
    return render_template('Report.html', username=username)

if __name__ == '__main__':
    app.run(debug = True)