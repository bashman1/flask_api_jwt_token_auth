from flask import request, Blueprint, jsonify, make_response
from api.controllers.users_controller import UserController

users_bt = Blueprint('auth', __name__)
users_controller = UserController()

@users_bt.route('/auth')
def get_users():
    return users_controller.get_users()

@users_bt.route('/auth/<int:userId>')
def get_user(userId):
    return users_controller.get_user(userId)

@users_bt.route('/auth/register', methods=['POST'])
def register_user():
    data = request.get_json()
    return users_controller.create_user(data)

@users_bt.route('/auth/login', methods=['POST'])
def login_user():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            auth_token = auth_header.split(" ")[1]

        except IndexError:
            return make_response(jsonify({
                'message':'Bearer token malformed.'
            }))

    else:
        auth_token = ''

    data = request.get_json()
    return users_controller.login(auth_token, data)