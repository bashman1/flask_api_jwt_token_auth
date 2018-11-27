import os, datetime
import jwt
import api

class AuthHelper():
    def __init__(self):
        self.secret_key = "test_api_len_key"

    def encode_auth_token(self, user_id):
        
        try:
            payload = {
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': str(user_id)
            }
            print(self.secret_key)
            return jwt.encode(
                payload,
                self.secret_key,
                algorithm = 'HS256'
            )

        except Exception as identifier:
            return identifier

    def decode_auth_token(self, authtoken):
        try:
            payload = jwt.decode(authtoken, self.secret_key)
            
            return payload['sub']
        
        except jwt.ExpiredSignatureError:
            return 'The token has expired. Please log in again'
        except jwt.InvalidTokenError:
            return 'invalid token. Please login again'