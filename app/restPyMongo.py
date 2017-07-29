"""
AUTHOR : PRATIK DHAGE
RESTful API using flask, PyMongo, MongoDB for the collection cities
"""
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'rest_python_mongo'
app.config['MONGO_URI'] = 'mongodb://pratikdhage:thedarkknightrises@ds119223.mlab.com:19223/rest_python_mongo'

mongo = PyMongo(app)


@app.route('/')
def about_cities():
    return render_template('cities.html')


# HTTP GET request for displaying all cities
@app.route('/cities', methods=['GET'])
def get_all_cities():
    cities = mongo.db.cities
    results = []
    for q in cities.find():
        results.append({'cname': q['cname'], 'state': q['state']})
    return jsonify({'result': results})


# HTTP GET request for displaying a particular city
@app.route('/cities/<string:cname>', methods=['GET'])
def get_city(cname):
    cities = mongo.db.cities
    q = cities.find_one({'cname': cname})
    if q:
        output = {'cname': q['cname'], 'state': q['state']}
    else:
        output = 'Sorry !....no results found.'
    return jsonify({'output': output})


# HTTP POST request for adding new city
@app.route('/cities', methods=['POST'])
def add_city():
    cities = mongo.db.cities
    cityname = request.json['cname']
    state = request.json['state']
    city_id = cities.insert({'cname': cityname, 'state': state})
    new_city = cities.find_one({'_id': city_id})
    output = {'cname': new_city['cname'], 'state': new_city['state']}
    return jsonify({'output': output})


# HTTP PUT request for modifying existing city city
@app.route('/cities/<string:cname>', methods=['PUT'])
def update_city(cname):
    cities = mongo.db.cities
    data = request.get_json()
    q = cities.find_one({'cname': cname})
    if q:
        output = data['cname']
        mongo.db.cities.update_one({'cname': cname}, {'$set': data})
    else:
        output = 'Sorry !....no results found.'
    return jsonify({'cname': output})


# HTTP DELETE request for deleting/removing a particular city
@app.route('/cities/<string:cname>', methods=['DELETE'])
def delete_city(cname):
    cities = mongo.db.cities
    q = cities.find_one({'cname': cname})
    if q:
        output = q['cname']
        mongo.db.cities.delete_one({'cname': cname})
    else:
        output = 'Sorry !....no results found.'
    return jsonify({'deleted': output})


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
