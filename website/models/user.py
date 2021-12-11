from .. import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True, unique=True)  # primary key is id
    admin = db.Column(db.String(5))  # if user is an admin
    fullname = db.Column(db.String(50))  # fullname of user
    email = db.Column(db.String(50), unique=True)  # email of user is unique
    password = db.Column(db.String(50))  # password of user
    status = db.Column(db.String(10))  # status of user (Active / Deleted)

    def __init__(self, fullname, email, password):
        """
        constructor
        :param fullname: String
        :param email: String
        :param password: String
        """
        self.admin = 'False'  # initially user are not admin
        self.fullname = fullname
        self.email = email
        self.password = generate_password_hash(password, 'sha256')  # password is stored as hash
        self.status = 'Active'  # initially all users will be considered active
