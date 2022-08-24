from flaskapp import db, bcrypt
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pw_hash = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    email_verified = db.Column(db.Boolean, nullable=False, default=False)
    acct_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_used = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.id} {self.username} {self.email}>'
    
    def __str__(self):
        return f'<User {self.username}>'