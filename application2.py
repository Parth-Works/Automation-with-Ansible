import flask
import time
import socket
import os

os_info = os.uname()
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

app = flask.Flask(__name__)

@app.route('/')
def index():
    Time= time.strftime("%H:%M:%S")
    return Time+" This Service is from the Host:  "+os_info+"  "+h_name+" ("+IP_addres+"). \n"
