import atexit
import psycopg2
from datetime import datetime
from config import config

"""
Database Info: the database is a postgresql 12 database hosted on google cloudsql. Credentials are hidden but stored in database.ini
config.py parses the credentials and allows the DataManager class to  access the database directly

Database: database
User: postgres

Table: parties
- code
- name
- date

Table: party_images
- code
- image_url

"""

class DataManager:
    def __init__(self):
        """
        Summary: Class for managing the database
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

    def addEvent(self, data):
        """
        Summary: Adds a new event to the database
        """

        code = data['code']
        name = data['name']
        date = data['date']
        images = data['images']

        print(code, name, date, images)
        # add event to parties table
        self.cur.execute("INSERT INTO parties (code, name, date) VALUES (%s, %s, %s)", (code, name, date))
        # add all the image urls to the party_images table
        for image in images:
            self.cur.execute("INSERT INTO party_images (code, image_url) VALUES (%s, %s)", (code, image))
        # update db
        self.conn.commit()

    def getEventImages(self, code):
        """
        Summary: retreives image urls for a particular event code
        """

        # execute SQL command and retreive results
        self.cur.execute("SELECT image_url FROM party_images WHERE code = (%s)", (code,))
        rawResult = self.cur.fetchall()
        print("RAW:", rawResult)
        # parse results into a list of urls
        result = []
        for tpl in rawResult:
            result.append(tpl[0])
        print("RESULT:", result)

        return result

    def testCode(self, code):
        """
        Summary: tests an event code for uniqueness in the database
        """

        self.cur.execute("SELECT code FROM parties")
        result = self.cur.fetchall()
        for tpl in result:
            if tpl[0] == code:
                return False
        return True

    def cleanup(self):
        """
        Summary: close the connection to the database on termination
        """

        print("Running cleanup...")
        self.conn.close()
