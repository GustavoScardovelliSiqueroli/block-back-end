import uuid
from bloggers.ext.database import db
from bloggers.api.models.post_contents import Postcontets
from sqlalchemy import delete

class PostContentsService():
    def teste(self):
        return 'teste'

    def add_post_contents(self, post_content: Postcontets) -> None:
        try:
            db.session.add(post_content)
            db.session.commit()
        except:
            raise Exception('Error in add post_content in db')
        
    def create_post_content(self, idpost: uuid.UUID, sequence: int, **kwargs) -> Postcontets:
        return Postcontets(idpostcontent=uuid.uuid4(), idpost=idpost, sequence=sequence,
         contenttext=kwargs.get('contenttext'),imagepath=kwargs.get('imagepath'))

    def delete_post_content(self, idpostcontent):
        print(idpostcontent)
        stmt = delete(Postcontets).where(Postcontets.idpostcontent == str('cd071cd7-a328-4adc-b844-8550050e9af5')) #type: ignore
        db.session.execute(stmt)
        db.session.commit()
        return 'ok'