# flask-sqlalchemy
This project is based on flask and SQL Alchemy performing CRUD operations .
Requirements :
  1.Python and Visual studio 
  2.postman - for running CRUD methods 

Installations that needed are:
$ pip install flask

$ pip install flask-sqlalchemy 
 
In your terminal you need to run this code for creation of database.
  python-check whether installed or not
  from movies import db 
  #click enter 
  db.create_all()

To run this project :
$ python Api.py ,you get a localhost http://localhost:5000/ 
instead open the link in postman to test the api.py 

use the following syntax for sending or retrieving requests:
1. GET  http://localhost:5000/ to run the localhost
2. POST http://localhost:5000/movies to add a new movie to database
3. PUT http://localhost:5000/movies/1 to update an existing data
4. DELETE http://localhost:5000/movies/1 to delete the existing data 
5. GET http://localhost:5000/movies to know the current data . 
