from flask_restplus import Namespace, Resource, fields
from server.namespaces.user import user_ns

user_model = user_ns.model('UserModel', {
    '_id': fields.String(),
    'username': fields.String(),
    'password': fields.String()
})
