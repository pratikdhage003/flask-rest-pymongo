# flask-rest-pymongo
# AUTHOR : PRATIK DHAGE

This is a RESTful web application for cities, implmented using
Flask, Python 3.6, MongoDB, PyMongo, virtualenv, pip, postman and remote mLab server for MongoDB database.

# How to Run :
python3.6 ./restPyMongo.py inside flaskvirtualenvironment


# restPyMongo.py is the file containing all RESTful URI's implemented using HTTP methods as follows :

In postman type 127.0.0.1:5000/cities
HTTP GET request for displaying all cities
@app.route('/cities', methods=['GET'])
def get_all_cities()

In postman type 127.0.0.1:5000/cities/<city_name>
HTTP GET request for displaying a particular city
@app.route('/cities/<string:name>', methods=['GET'])
def get_city(name)

In postman type 127.0.0.1:5000/cities
HTTP POST request for adding new city
@app.route('/cities', methods=['POST'])
def add_city()


In postman type 127.0.0.1:5000/cities/<city_name>
HTTP PUT request for modifying existing city city
@app.route('/cities/<string:name>', methods=['PUT'])
def update_city(name)


In postman type 127.0.0.1:5000/cities/<city_name>
HTTP DELETE request for deleting/removing a particular city
@app.route('/cities/<string:name>', methods=['DELETE'])
def delete_city(name)