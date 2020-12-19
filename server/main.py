import json
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

HOST = '0.0.0.0'
PORT = '4200'

@app.route('/')
def home():
    """
    Summary: serves index.html file to clients connecting on the home page
    """
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host=HOST, port=PORT)