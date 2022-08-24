from flaskapp import bcrypt
from flaskapp.models import User

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.pw_hash, password):
        return user
    return None

def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()