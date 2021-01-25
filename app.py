from flask import Flask,request
import socket
from flask import jsonify
import flask_cors CORS, cross_origin
app = Flask(__name__)
CORS(app, resources={r'*': {'origins': 'http://localhost:8081/'}})
@app.route('/', methods=['GET', 'POST'])
def index():
    print("gt")
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request)
    print("gt")
    return 'login'
    
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return 'logout'


if __name__ == "__main__":
    app.run(host='localhost', port=5003, debug=True)