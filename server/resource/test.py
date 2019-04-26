from flask_restplus import Namespace, Resource, fields

api = Namespace('test', description='API test')

test_get_model = api.model('TestGetModel', {
    'test': fields.Boolean(required=True)
})

test_post_model = api.model('TestPostModel', {
    'test': fields.Boolean(required=True),
    'query': fields.String(required=True)
})

test_form_model = api.model('TestUserModel', {
    'query': fields.String(required=True)
})

@api.route('/')
class Test(Resource):
    @api.marshal_with(test_get_model)
    def get(self):
        return {
            'test': True
        }

    @api.expect(test_form_model, validate=True)
    @api.marshal_with(test_post_model)
    def post(self):
        return {
            'test': True,
            'query': api.payload['query']
        }
