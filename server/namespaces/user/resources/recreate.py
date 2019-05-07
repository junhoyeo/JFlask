from flask_restplus import Resource
from server.namespaces.user import user_ns
from server.namespaces.user.models import user_form_model

from flask import jsonify, request
from server import mongo


@user_ns.route('/recreate')
class Recreate(Resource):
    @user_ns.expect(user_form_model, validate=True)    
    @user_ns.doc(
        responses={200: '성공', 400: '잘못된 요청', 500: 'Unacknowledged'},
        description='이전의 사용자 오브젝트를 import합니다.')
    def post(self):
        user = user_ns.payload
        result = mongo.db.users.insert_one(user)
        if not result.acknowledged:
            return {}, 500
        return {}, 200
