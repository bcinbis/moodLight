"""
File for dealing with messaging interaction with server
"""
import urllib.request
import requests 
class Client:
    def __init__(self, code, serverAddress):
        self.partyCode = code
        self.serverAddress = serverAddress

    def getImageUrls(self, code):
        params = {
            'partycode': code
        }
        return requests.get(f"http://{self.serverAddress}/get-images", params=params).json()

    def downloadImages(self, urls):
        for i in range(len(urls)):
            file = open(str(i)+'.jpg','wb')
            file.write(requests.get(urls[i]).content)
            file.close()


if __name__ == "__main__":
    SERVER = '35.239.118.105:4200'
    CODE = 'AAA'
    URLS = ["https://storage.googleapis.com/party_images/dont%20enter.jpg", "https://storage.googleapis.com/party_images/green%20light.jpg"]

    client = Client(CODE, SERVER)
    client.downloadImages(URLS)
    


    