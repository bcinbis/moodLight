import atexit
import psycopg2
from datetime import datetime
from config import config

"""
Database: PARTIES

Table: parties
- code
- name
- date

Table party_images
- code
- image_url
"""

class DataManager:
    def __init__(self):
        """
        Summary: Class for managing the data
        """
        print('Starting DB Manager')
        # Obtain the configuration parameters
        params = config()
        # Connect to the PostgreSQL database
        self.conn = psycopg2.connect(**params)
        # Create a new cursor
        self.cur = self.conn.cursor()
        # Define cleanup function
        atexit.register(self.cleanup)

    def addParty(self):
        pass

    def getPartyImages(self, code):
        # execute SQL command and retreive results
        self.cur.execute("SELECT image_url FROM party_images WHERE code == (%s)", (code))
        rawResult = self.cur.fetchall()
        # parse results into a list of urls
        result = []
        for tpl in rawResult:
            result.append(tpl[1])
            
        return result