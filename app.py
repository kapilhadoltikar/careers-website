# this imports Flak class from flask module 
from flask import Flask, render_template

# this is an object of an Flask class named app and variable __name__
app = Flask(__name__)

# 
@app.route("/")
def hello_world():
    return render_template('home.html')


# this will run app without cli input
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)