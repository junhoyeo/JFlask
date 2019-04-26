from flask_restplus import Namespace, Resource, fields

api = Namespace('auth', description='User authentication')

@api.route('/test')
class AuthTest(Resource):
    @ns.expect(book_model)
    def get(self):
        return {
            'test': True
        }
