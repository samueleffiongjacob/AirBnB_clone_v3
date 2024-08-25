# Take your tim to read below

[Learn REST: A RESTful Tutorial](https://www.restapitutorial.com/)
[Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
[HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
[Flask cheatsheet](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/301/flask_cheatsheet.pdf)
[What are Flask Blueprints, exactly?](https://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly)
[Flask](https://palletsprojects.com/projects/flask/)
[Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
[Flask tests](https://flask.palletsprojects.com/en/1.1.x/testing/)
[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
[“404 page”, a “Not found”… 34 brilliantly designed 404 error pages](https://www.creativebloq.com/web-design/best-404-pages-812505)

## REST API

REST API is a software architectural style for Backend.

REST = “REpresentational State Transfer”. API = Application Programming Interface

Its purpose is to induce performance, scalability, simplicity, modifiability, visibility, portability, and reliability.

REST API is Resource-based, a resource is an object and can be access by a URI. An object is “displayed”/transferred via a representation (typically JSON). HTTP methods will be actions on a resource.

Example:

Resource: Person (John)
Service: contact information (GET)
Representation:
first_name, last_name, date_of_birth
JSON format
There are 6 constraints:

1. Uniform Interface
Define the interface between client-server
Simple and can be split in small parts
HTTP verbs
GET:
Read representation of a resource or a list of resources
POST:
Create a new resource
PUT:
Update an existing resource
DELETE:
Remove an existing resource
URIs - resource name
A resource representation is accessible by a URI:

GET /users: path for listing all user resources
GET /users/12: path for the user id = 12
GET /users/12/addresses: path for listing all addresses of the user id = 12
POST /users: path for creating a user resource
PUT /users/12: path for updating the user id = 12
DELETE /users/12/addresses/2: path for deleting the address id = 2 of the user id = 12
HTTP Response
In the HTTP Response, the client should verify the information of two things:

status code: result of the action
body: JSON or XML representation of resources
Some important status code:

200: OK
201: created => after a POST request
204: no content => can be return after a DELETE request
400: bad request => the server doesn’t understand the request
401: unauthorized => client user can’t be identified
403: forbidden => client user is identified but not allowed to access a resource
404: not found => resource doesn’t exist
500: internal server error
2. Stateless
The server is independent of the client. The server doesn’t store user client information/state. Each request contains enough context to process it (HTTP Headers, etc.)

Some authentication systems like OAuth have to store information on the server side but they do it with REST API design.

3. Cacheable
All server responses (resource representation) are cacheable:

Explicit
Implicit
Negotiated
Caches are here to improve performances. In a REST API, clients don’t care about the caching strategy, if the resource representation comes from a cache or from a database…

4. Client-Server
REST API is designed to separate Client from the Server. The server doesn’t know who is talking to it. Clients are not concerned with data storage => the portability of client code is improved. Servers are not concerned with the user interface or user state so that servers can be simpler and more scalable

5. Layered System
Client can’t assume direct connection to server. Intermediary servers may improve system scalability by enabling load-balancing and by providing shared caches. Layers may also enforce security policies.

6. Code on Demand (optional)
Server can temporarily:

Transfer logic to client
Allow client to execute logic
Example: JavaScript

## if u are useing alx sandbox alway restart my sql

```bash
# command
$ sudo service mysql restart

# or 
$ sudo apt update

# connect
$ sudo mysql

# run query
$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -
$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db  # password: 
$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p # password: hbnb_test_pwd
$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
```

## task

```bash
# command 
$ pip install flask
$ pip install Flask-CORS
$ pip install SQLAlchemy
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
$ sudo apt-get update
$ sudo apt-get install pkg-config

$ pip3 install mysqlclient
$ python3 -c "import MySQLdb" # if no output or error installation succeful



# task 1 : Never fail!
$ python3 -m unittest discover tests 2>&1 | tail -1
$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1

# task 2 :  Improve storage
# let add dummy state 
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./add_states.py

# test 
$ cat test_get_count.py
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./test_get_count.py 
$ ./test_get_count.py 

# task 3
# Status of your API
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app

# in another terminal
$ curl -X GET http://0.0.0.0:5000/api/v1/status
$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type

# task 4 : Some stats?
# create and end point
$ curl -X GET http://0.0.0.0:5000/api/v1/stats

# Task 5 :  Not found
# In api/v1/app.py, create a handler for 404 errors that returns a JSON-formatted 404 status code response. The content should be: "error": "Not found"
$ curl -X GET http://0.0.0.0:5000/api/v1/nop
$ curl -X GET http://0.0.0.0:5000/api/v1/nop -vvv

# task 6: state
# make sure dev server is still running
$ curl -X GET http://0.0.0.0:5000/api/v1/states/
$ curl -X GET http://0.0.0.0:5000/api/v1/states/fd53942e-d693-4a4b-a363-9a50a1c3ae2c
$ curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "California"}' -vvv
$  curl -X PUT http://0.0.0.0:5000/api/v1/states/d137e404-8561-413d-891b-a0004061e600 -H "Content-Type: application/json" -d '{"name": "California is so cool"}'
$ curl -X GET http://0.0.0.0:5000/api/v1/states/d137e404-8561-413d-891b-a0004061e600
$ curl -X DELETE http://0.0.0.0:5000/api/v1/states/c761225b-7214-48b7-91bf-33f89168c9ce
$ curl -X GET http://0.0.0.0:5000/api/v1/states/c761225b-7214-48b7-91bf-33f89168c9ce

# task : 7. City
# just repeat the steps below

# 8. Amenity
# do above for amenty

# 9. User
# just reapet for the others
```
