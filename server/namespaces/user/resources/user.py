from flask_restplus import Resource
from server.namespaces.user import user_ns
from server.namespaces.user.models import user_model

from bson import ObjectId
from flask import jsonify
from server import mongo


@user_ns.route('/<ObjectId:id>')
class User(Resource):
    @user_ns.marshal_with(user_model)
    @user_ns.doc(
        responses={200: '성공', 404: '존재하지 않는 _id'},
        description='`_id`를 가지는 사용자 정보를 가져옵니다.')
    def get(self, id):
        print(id)
        user = mongo.db.users.find_one_or_404({'_id': id})
        user['_id'] = str(user['_id'])
        return jsonify(user)
