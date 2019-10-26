The Great Bookshelf of Udacity
This project is a virtual bookshelf for Udacity students. Students are able to add their books to the bookshelf, give them a rating, update the rating and search through their book lists. As a part of the Fullstack Nanodegree, it serves as a practice module for lessons from Course 2: API Development and Documentation. By completing this project, students learn and apply their skills structuring and implementing well formatted API endpoints that leverage knowledge of HTTP and API development best practices.

All backend code follows PEP8 style guidelines.

Getting Started

Base URL: At present this app can only be run locally and is not hosted as a base URL. 
The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
Authentication: This version of the application does not require authentication or API keys.


Error Handling:

Errors are returned as JSON objects in the following format:

{
    'success' : False,
    'error' : 400,
    'message': "bad request"
}

The API will return three error types when requests fail:

400: Bad request
404: Resource Not Found
422: Not Processable

Endpoints:

GET /books

General

    Returns a list of book objects, successful value, and total number of books
    Results are paginated in groups of 8. Include a request argument to choose page number, starting from 1.

Sample

    curl http://127.0.0.1:5000/books

    { 
   "books":[ 
      { 
         "author":"Daniel Kahneman",
         "id":1,
         "rating":9,
         "title":"Thinking Fast and Slow"
      },
      { 
         "author":"Nasim Taleb",
         "id":2,
         "rating":8,
         "title":"Fooled By Randomness"
      },
      { 
         "author":"William Blake",
         "id":3,
         "rating":10,
         "title":"Superforecasting"
      },
      { 
         "author":"George R.R Martin",
         "id":4,
         "rating":8,
         "title":"Feast for the Crows"
      }
   ],
   "success":true,
   "total_books":4
}

