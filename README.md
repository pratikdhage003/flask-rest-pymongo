# AUTHOR : PRATIK DHAGE
# flask-rest-pymongo

This is a RESTful web application for cities, implemented using
Flask, Python 3.6, MongoDB, PyMongo, virtualenv, pip, postman and remote mLab server for MongoDB database.

# How to Run :
python3.6 ./restPyMongo.py inside flaskvirtualenvironment


# restPyMongo.py is the file containing all RESTful URI's implemented using HTTP methods as follows :

In postman type 127.0.0.1:5000/ ---->
@app.route('/')
def about_cities():

In postman type 127.0.0.1:5000/cities  ---->
@app.route('/cities', methods=['GET'])
def get_all_cities()

In postman type 127.0.0.1:5000/cities/<city_name>  ---->
@app.route('/cities/<string:name>', methods=['GET'])
def get_city(name)

In postman type 127.0.0.1:5000/cities  ---->
@app.route('/cities', methods=['POST'])
def add_city()


In postman type 127.0.0.1:5000/cities/<city_name>  ---->
@app.route('/cities/<string:name>', methods=['PUT'])
def update_city(name)


In postman type 127.0.0.1:5000/cities/<city_name>  ---->
HTTP DELETE request for deleting/removing a particular city
@app.route('/cities/<string:name>', methods=['DELETE'])
def delete_city(name)