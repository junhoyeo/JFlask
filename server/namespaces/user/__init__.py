from flask_restplus import Namespace

user_ns = Namespace('user', description='User resources')

# resources
import server.namespaces.user.resources.user
import server.namespaces.user.resources.user_all
