import six
from flask import Blueprint, Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api, Resource
# Import the database object from the main app module
from app import db , app

api_v1 = Api(app)

# Define the blueprint: 'api', set its url prefix: api.url/api
api = Blueprint('api', __name__)

# Set the route and accepted methods


class UserAPI(Resource):

    def get(self, id):
        return {"test": "test"}

    def put(self, id):
        pass

    def delete(self, id):
        pass


api_v1.add_resource(UserAPI, '/api/v1/users/<int:id>', endpoint='user')
