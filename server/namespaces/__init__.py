from flask_restplus import Api

api = Api(
    title='Jflask',
    version='1.0',
    description='Framework for Flask RESTful API and management',
)

from server.namespaces.test import test_ns
api.add_namespace(test_ns, path='/test')
