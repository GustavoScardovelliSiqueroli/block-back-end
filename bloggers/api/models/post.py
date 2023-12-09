from bloggers.ext.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import TEXT

from datetime import date
from uuid import UUID

class Posts(db.Model):
    __tablename__ = 'posts'
    idpost = db.Column(db.String(255), primary_key=True, nullable=False, unique=True)
    iduser = db.Column(db.String(255), ForeignKey('users.id'), nullable=False)
    idsequence = db.Column(db.String(255), ForeignKey('posts.idpost'), nullable=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(TEXT, nullable=True)
    createdat = db.Column(db.Date, nullable=False)
    deletedat = db.Column(db.Date, nullable=True)

    def __init__(self, idpost: UUID, iduser: UUID, title: str, createdat: date, text: str|None = None, idsequence: UUID|None = None) -> None:
        """A model for Posts db
        Args:
            idpost (UUID): the post id
            iduser (UUID): the user id
            idsequence (UUID): the sequence id
            title (str): the post title
            text (str): the post text
            createdat (date): the post created date
        """
        self.idpost = idpost.__str__()
        self.iduser = iduser.__str__()
        self.title = title        
        self.createdat = createdat.__str__()    
        self.idsequence = idsequence.__str__()        
        self.text = text        
        self.deletedat = None      

