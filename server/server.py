import json

from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from pprint import pprint
from dataManager import DataManager

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./templates/css')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

HOST = '0.0.0.0'
PORT = '4200'

@app.route('/index.html')
def home():
    """
    Summary: serves index.html file to clients connecting on the home page
    """
    return render_template('index.html')

@app.route('/create.html')
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
    app.run(host=HOST, port=PORT)