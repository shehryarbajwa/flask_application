import os
import unittest
import json
import sys
from  flask_sqlalchemy import SQLAlchemy
from application.app.flaskr.__init__.py import create_app
from application.app.flaskr.models.py import setup_db, Book

class BookCaseTest(unittest.TestCase):
    """This class represents the trivia test case"""

    def isUpper(self):
        self.assertEqual('FOO'.isupper())
    
    def setUp(self):
        #Create the app
        self.app = create_app()
        #Allows the client to set up test_client for us to start testing the application
        self.client = self.app.test_client
        self.database_name = 'bookshelf_test'
        self.database_path = 'postgres://{}@{}/{}'.format('shehryarbajwa', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Anansi boys',
            'author' : 'Neil Gaiman',
            'rating': 5
        }

    def tearDown(self):
        pass

    def test_get_paginated_books(self):
        res = self.client().get('/books')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        #Assert true that there is a number of total_books. In case, there are no books, this will return None
        self.assertTrue(data['total_books'])
        #Assert true that there is a len of the value books. In case there are no books, this will return None
        self.assertTrue(len(data["books"]))

    def test_404_sent_requesting_beyond_valid_page(self):
        #The json body is just to show whether there is any json
        #In this case it is none so we dont really need it
        # res = self.client().get('/books?page=1000', json={'rating': 1})
        res = self.client().get('/books?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    


        

if __name__ == "__main__":
    unittest.main()