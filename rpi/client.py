"""
File for dealing with messaging interaction with server
"""

import requests 
class Client:
    def __init__(self, code, serverAddress):
        self.partyCode = code
        self.serverAddress = serverAddress

    def getImages(self):
        params = {
            'partycode': self.partyCode
        }
        return requests.get(f"http://{self.serverAddress}/get-images", params=params).json()

