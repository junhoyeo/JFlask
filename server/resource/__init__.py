from flask_restplus import Api

from server.resource.test import api as ns_test

api = Api(
    title='Jflask',
    version='1.0',
    description='A example of RESTful Flask API',
)

api.add_namespace(ns_test, path='/test')
