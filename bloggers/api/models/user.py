from bloggers.ext.database import db

from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(254), primary_key=True, nullable=False)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(86), unique=True, nullable=False)
    password = db.Column(db.String(86), nullable=False)

    def __init__(self, name: str, email: str, pwd: str):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.password = generate_password_hash(str(pwd), method='pbkdf2:sha1', salt_length=8)
