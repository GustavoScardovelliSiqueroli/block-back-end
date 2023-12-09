from cgitb import text
from datetime import date
import uuid
from bloggers.api.models.post import Posts
from bloggers.ext.database import db

class PostsService():

    def add_post(self, post: Posts) -> None:
        """add a post in db
        Args:
            post (Posts): a post with Posts model
        Raises:
            Exception: ERROR IN ADD POST IN DB
        """
        try:
            db.session.add(post)
            db.session.commit()
            db.session.close()
        except:
            raise Exception('Error in add post in db')
        
    def create_post(self, iduser: uuid.UUID, title: str, **kwargs) -> Posts:
        """create a post model Posts
        Args:
            iduser (uuid.UUID): user that create the post
            title (str): the post title
            kwargs:
                text (str): the post text
                idsequence (UUID): the post sequence if exist
        Returns:
            Posts: the post
        """
        return Posts(uuid.uuid4().__str__(), iduser, title, date.today().__str__(), text=kwargs.get('text'), idsequence=kwargs.get('idsequence'))