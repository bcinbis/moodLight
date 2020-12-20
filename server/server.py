import json

from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from pprint import pprint
from dataManager import DataManager

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

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/get-images', methods=['GET'])
def getImages():
    eventCode = request.args.get('eventcode')
    images = dbManager.getEventImages(eventCode)
    return json.dumps(images)


@app.route('/create-event', methods=['POST'])
def createEvent():
    payload = request.get_data().decode('utf-8')
    payload = json.loads(payload)
    pprint(payload)
    dbManager.addEvent(payload)
    response = {'Response': 'Event created'}
    return json.dumps(response)

if __name__ == '__main__':
    dbManager = DataManager()
    socketio.run(app, host=HOST, port=PORT)