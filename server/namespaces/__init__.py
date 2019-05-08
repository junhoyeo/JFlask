import base64
import hashlib
import types
from flask_restplus import Api


def extend_namespace(ns):
    def add_resources(ns, *resources):
        for resource in resources:
            __import__(
                'server.namespaces.{}.resources.{}'.format(
                    ns.name, resource))
    ns.add_resources = types.MethodType(add_resources, ns)


def hash_password(password):
    return base64.b64encode(hashlib.sha512(
        password.encode('UTF-8')
    ).digest()).decode()


api = Api(
    title='JFlask',
    version='1.0',
    description='Template for Flask RESTful API and management',
)

from server.namespaces.test import test_ns
api.add_namespace(test_ns, path='/test')

from server.namespaces.user import user_ns
api.add_namespace(user_ns, path='/user')

from server.namespaces.auth import auth_ns
api.add_namespace(auth_ns, path='/auth')
