import os
from flask import Flask
app = Flask(__name__)

# print(os.environ['environment'])

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    