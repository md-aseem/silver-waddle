from datetime import datetime

from flask_login import UserMixin

from src import bcrypt, db

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False, server_default='')
    last_name = db.Column(db.String, nullable=False, server_default='')
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    file_path = db.Column(db.String, nullable=False, server_default='')
    word_count = db.Column(db.Integer, nullable=False, server_default='0')
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, first_name, last_name, email, password, file_path, word_count, is_admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.file_path = file_path
        self.word_count = word_count
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<email {self.email}>"