from operator import pos
from bloggers.ext.database import db
from bloggers.api.models.post import Posts
from sqlalchemy import select, delete

from datetime import date
import uuid

class PostsService():

    def add_post(self, post: Posts) -> None:
        """add a post in db
        Args:
            post (Posts): a post with Posts model
        Raises:
            Exception: ERROR IN ADD POST IN DB
        """
        print(post.to_dict())
        try:
            db.session.add(post)
            db.session.commit()
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
        return Posts(uuid.uuid4(), iduser, title, date.today(), text=kwargs.get('text'), idsequence=kwargs.get('idsequence'))

    def selecta_ll_posts(self) -> dict | None:
        try:
            stmt = select(Posts)  
            result = db.session.execute(stmt).all()
           
            if result:
                post_list: list[dict] = []
                for posts in result:
                    for post in posts:
                        postdict = {'idpost': post.idpost,
                                    'iduser': post.iduser,
                                    'title': post.title,
                                    'text': post.text,
                                    'createdat': post.createdat.__str__(),
                                    'sequence': post.idsequence,
                                    'deletedat': post.deletedat}
                        post_list.append(postdict)
                return {'posts': post_list} 
            return None
        except:
            raise Exception('error in list posts')

    def delete_post(self, idpost) -> None:
        try:
            stmt = delete(Posts).where(Posts.idpost == idpost) #type: ignore
            db.session.execute(stmt)
            db.session.commit()
        except:
            Exception('Error in delete post')        

    def find_post(self, idpost) -> None | Posts:
        try:
            stmt = select(Posts).where(Posts.idpost == idpost)
            result = db.session.execute(stmt).first()
            if result:
                post: Posts = result[0]
                return post
        except:
            Exception('Error in find post')