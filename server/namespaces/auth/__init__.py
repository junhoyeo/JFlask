from flask_restplus import Namespace
from server.namespaces import extend_namespace

auth_ns = Namespace('auth', description='User authentication')
extend_namespace(auth_ns)

auth_ns.add_resources('auth')
