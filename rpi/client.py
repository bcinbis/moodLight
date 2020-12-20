"""
File for dealing with messaging interaction with server
"""
# Imports from downloaded libaray
import urllib.request
import requests 


class Client:
    '''
    This class creates handles requests to get images (corresponding to event code) from server
    Also downloads said images into the img directory
    '''
    def __init__(self, serverAddress):
        # Setup with constant server address on Google Cloud
        self.serverAddress = serverAddress

    def getImageUrls(self, code):
        # Sends get request for all of the images belonging to the event user has code for
        # Recieves list of image URLs
        params = {
            'eventcode': code
        }
        return requests.get(f"http://{self.serverAddress}/get-images", params=params).json()

    def downloadImages(self, urls):
        # Download each of the above images through their URL and store in ~/img/
        for i in range(len(urls)):
            file = open('./img/'+str(i)+'.jpg','wb')
            file.write(requests.get(urls[i]).content)
            file.close()


if __name__ == "__main__":
    SERVER = '35.239.118.105:4200'
    CODE = 'abc'
    client = Client(SERVER)
    urls = client.getImageUrls(CODE)
    client.downloadImages(urls)
    


    