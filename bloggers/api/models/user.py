from bloggers.ext.database import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(254), primary_key=True, nullable=False)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(86), unique=True, nullable=False)
    password = db.Column(db.String(86), nullable=False)
    createdat = db.Column(db.Date)
    

    def __init__(self, id: str,  name: str, email: str, pwd: str, createdat: str) -> None:
        """A model for users of system
        Args:
            id (str): the user id
            name (str): the user name
            email (str): the user email
            pwd (str): the user password
            createdat (str): date that user was created
        """
        self.id = id
        self.name = name
        self.email = email
        self.password = pwd
        self.createdat = createdat
