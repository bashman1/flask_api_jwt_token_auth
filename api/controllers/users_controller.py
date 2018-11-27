from flask import make_response, jsonify, request
from api.models.user_model import UserModel
from api.utilities.auth_helpers import AuthHelper


class UserController():

    def __init__(self):
        self.user_model =  UserModel()
        self.auth_helper = AuthHelper()

    def get_user(self, userId):
        user_model = UserModel()

        user = user_model.get_user(userId)
        if not user or user is None:
            return make_response(jsonify({
                'message ':'user not found'
            }), 200)
        return make_response(jsonify({
                'message ':'success',
                'user': user
            }), 200)

    def get_users(self):
        user_model = UserModel()

        users = user_model.get_all_users()
        if not users or len(users) < 1 or users is None:
            return make_response(jsonify({
                'message ':'no user was found'
            }), 200)
        return make_response(jsonify({
                'message ':'success',
                'user': users
            }), 200)

    def create_user(self, args):

        try:
            user = self.user_model.create_user(args)

            if not user or user is None:
                return make_response(jsonify({
                    'message': 'Sorry! user was not created'
                }), 400)

            print(user)
            print((user['user_id']))
            user_id = user["user_id"]
            auth_token = self.auth_helper.encode_auth_token(user_id)
            print((auth_token))

            if not auth_token or auth_token is None:
                return make_response(jsonify({
                    'message': 'user created but not authenticated. Please log in'
                }), 201)

            return make_response(jsonify({
                'message': 'success',
                'token': auth_token.decode("utf-8")
            }), 201)

        except Exception as ex:
            print(ex)
            return  make_response(jsonify({
                'message': 'errors occured'
            }), 400)

    def login(self, auth_token, args):

        if auth_token:
            user_id = self.auth_helper.decode_auth_token(auth_token)
            print(user_id)
            if not isinstance(user_id, str):
                return  make_response(jsonify({
                    'message':'wrong token'
                }))

            user = self.user_model.get_user(int(user_id))
            if not user or user is None:
                return make_response(jsonify({
                    'message':'user not found'
                }))
            return make_response(jsonify({
                'status':'logged in',
                'user':user
            }))

        else:
            return make_response(jsonify({
                'message':'provide valid token'
            }))




