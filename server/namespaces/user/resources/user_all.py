from flask_restplus import Resource
from server.namespaces.user import user_ns

from flask import jsonify, request
from server import mongo


@user_ns.route('/all')
class UserAll(Resource):
    def get(self):
        limit = request.args.get('limit', 100, type=int)
        skip = request.args.get('skip', 0, type=int)
        # cursor = mongo.db.users.find().limit(limit).skip(skip)
        # return list(cursor)
        cursor = mongo.db.users.find().limit(limit).skip(skip)
        users = list(cursor)
        for idx, user in enumerate(users):
            users[idx]['_id'] = str(user['_id'])
        return users
