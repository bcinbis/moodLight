"""
File for dealing with messaging interaction with server
"""
import urllib.request
import requests 
class Client:
    def __init__(self, serverAddress):
        self.serverAddress = serverAddress

    def getImageUrls(self, code):
        params = {
            'eventcode': code
        }
        return requests.get(f"http://{self.serverAddress}/get-images", params=params).json()

    def downloadImages(self, urls):
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
    


    