from db.models import User

def get_user(user_id):
    return User.read(user_id=user_id)

def save_user(user_object):
    return User.write(user_object)

