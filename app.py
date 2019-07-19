import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello There!<h1>"
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000)), debug=True )