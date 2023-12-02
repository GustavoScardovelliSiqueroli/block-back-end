from bloggers.ext.database import db
from bloggers.api.models.user_model import UserModel

class UserService():

    def add_user(name: str, email: str, pwd: str) -> None:
        """Add a user in db
        arguments: user: UserModel
        return: none
        return: Error
        """
        user = UserModel(name, email, pwd)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            print(20*'_' + 'ERROR' + 20*'_')
            raise Exception("Error on add user in db")
            print()


    def teste(self, txt: str) -> bool:
        """Verifica se existe um texto de parâmetro
        retunr: True
        return: False"""
        if txt:
            return bool(True)
        return bool(False)
    