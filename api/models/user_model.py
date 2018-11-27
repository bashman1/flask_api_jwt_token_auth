
users = []

class UserModel():
    def __init__(self):
        self.users = users
    
    def create_user(self, args):
        try:
            user = dict(
                user_id = len(users)+1,
                email = args['email'],
                first_name = args['first_name'],
                last_name = args['last_name'],
                phone_number = args['phone_number'],
                password = args['password']
            )

            users.append(user)
            return  user

        except Exception as identifier:
            return identifier

    def get_user(self, userId):

        for user in self.users:
            if user['user_id'] == userId:
                return user
        return None

    def get_all_users(self):
        return self.users