import os
import unittest
import json
from   flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book

class BookCaseTest(unittest.TestCase):
    """This class represents the trivia test case"""
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass


    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_get_paginated_books(self):
        res = self.client().get('/books')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        #Assert true that there is a number of total_books. In case, there are no books, this will return False
        self.assertTrue(data['total_books'])
        #Assert true that there is a len of the value books. In case there are no books, this will return False
        self.assertTrue(len(data["books"]))

    def test_404_sent_requesting_beyond_valid_page(self):
        #The json body is just to show whether there is any json
        #In this case it is none so we dont really need it
        res = self.client().get('/books?page=1000', json={'rating': 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_books(self):
        res = self.client().get('/books/3')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_book_rating(self):
        res = self.client().patch('/books/1', json=
        
        {
            'author': 'Nasim Taleb',
            'title': 'Antifragile',
            'rating': 1
        }
        )
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(book.format()['rating'],1)

    def test_400_for_failed_update(self):
        res = self.client().patch('/books/5', json={'rating': 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], 'bad request')

    def test_delete_data(self):
        res = self.client().delete('/books/1')
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertEqual(data['total_books'], 0)
        self.assertTrue(len(data['books']))
        self.assertEqual(book, None)

    def test_get_book_search_with_results(self):
        res = self.client().post('/books', json={'search': 'Novel'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_books'])
        self.assertEqual(len(data['books']), 4)

    def test_get_book_search_without_results(self):
        res = self.client().post('/books', json={'search': 'Applejack'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_books'])
        self.assertEqual(len(data['books']), 4)




    

    

        


if __name__ == "__main__":
    unittest.main()