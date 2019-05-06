from flask_restplus import Resource
from server.namespaces.user import user_ns

from bson import ObjectId
from flask import jsonify
from server import mongo


@user_ns.route('/<ObjectId:id>')
class User(Resource):
    def get(self, id):
        print(id)
        user = mongo.db.users.find_one_or_404({'_id': id})
        user['_id'] = str(user['_id'])
        return jsonify(user)
