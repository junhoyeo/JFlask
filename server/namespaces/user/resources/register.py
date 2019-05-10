from flask_restplus import Resource
from server.namespaces.user import user_ns
from server.namespaces.user.models import user_form_model

from functools import wraps
import validators
from flask import jsonify, request
from server import mongo
from server.namespaces import hash_password

def validate(ns, key, validator):
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not validator(ns.payload[key]):
                return { 'message': "'{}' field validation failed".format(key) }, 400
            return function(*args, **kwargs)
        return wrapper
    return real_decorator

@user_ns.route('/register')
class Register(Resource):
    @user_ns.expect(user_form_model, validate=True)
    @user_ns.doc(
        responses={200: '성공', 400: '잘못된 요청', 500: 'Unacknowledged'},
        description='새로운 사용자를 추가합니다.')
    @validate(user_ns, 'email', validators.email)
    def post(self):
        user = user_ns.payload
        user['password'] = hash_password(user['password'])
        result = mongo.db.users.insert_one(user)
        if not result.acknowledged:
            return {}, 500
        return {}, 200
