import json
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO

from dataManager import DataManager()

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

@app.route('/get-images')
def getImages():
    partyCode = request.args.get('partycode')
    images = dbManager.getPartyImages(partyCode)
    return json.dumps(images)

if __name__ == '__main__':
    dbManager = DataManager()``
    socketio.run(app, host=HOST, port=PORT)