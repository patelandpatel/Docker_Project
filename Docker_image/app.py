### flask app for hello world 

from flask import Flask 
import os 

app = Flask(__name__) # Flask is 

@app.route("/", methods=['GET'])
def home():
    return "Hello World"

@app.route("/about", methods=['GET'])
def about():
    return "This is the About page"

@app.route("/user/<name>", methods=['GET'])
def user(name):
    return f"Hello, {name}!"

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    ### with 0.0.0.0 you can access with local IP address(192....) or (127.0.0.1) and local host address(http://localhost:5000)

'''
Access at:

http://localhost:5000/ → "Hello World"
http://localhost:5000/about → "This is the About page"
http://localhost:5000/user/John → "Hello, John!"

'''