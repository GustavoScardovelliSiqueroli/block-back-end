from typing import Any
from bloggers.ext.database import db
from bloggers.api.models.user import User

from sqlalchemy import select
from werkzeug.security import check_password_hash, generate_password_hash
from re import search, match
from datetime import date
import uuid

class UserService():


    def create_user(self, name: str, email: str, pwd: str, **kwargs) -> User:
        """create a user with name, email, pwd salt hash and created date.
        Args:
            name (str): the user name
            email (str): the user email
            pwd (str): the user password
        Returns:
            User: user created
        """
        user_id = uuid.uuid4().__str__()
        user_createdat = date.today().__str__()
        user_pwd = generate_password_hash(str(pwd), method='pbkdf2:sha1', salt_length=8)
        return User(user_id, name, email, user_pwd, user_createdat, kwargs.get('isadm'))


    def add_user(self, user: User) -> None:
        """Add a user in db
        Args: 
            name (str): name of user
            email (str): email of user
            pwd (str): password of user
        Returns: 
            None
            raise Error
        """
        try:
            db.session.add(user)
            db.session.commit()
        except:
            print(20*'_' + 'ERROR' + 20*'_')
            raise Exception("Error on add user in db")


    def validation_pwd(self, pwd: str) -> str:
        """Validates that the password meets all requirements
        Args:
            pwd (str): the user password
        Returns:
            str: password if true
            str: msg if error 
        """
        error_password_messages = ['Senha deve conter ao menos 8 caracteres',
                        'Senha deve contaer ao menos uma letra MAIÚSCULA',
                        'Senha deve conter ao menos um número',
                        'Senha deve conter ao menos um caractere especial']

        if not search(r'.{8,}', pwd):
            return error_password_messages[0]
        if not search(r'[A-Z]', pwd):
            return error_password_messages[1]
        if not search(r'\d', pwd):
            return error_password_messages[2]
        if not search(r'[!@#$%¨&*]', pwd):
            return error_password_messages[3]
        return pwd


    def validation_email(self, email: str) -> str:
        """validates that the email meets all requirements
        Args:
            email (str): the user email
        Returns:
            str: email if true
            str: msg if error
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if match(pattern, email):
            return email
        return 'Email inválido!'
        

    def validation_name(self, name: str) -> str:
        """validates that the name meets all requirements
        Args:
            name (str): the user name
        Returns:
            str: name if true
            str: msg if error
        """
        return ''


    def exemplo(self, txt: str) -> bool:
        """Verifica se existe um texto de parâmetro
        return: True
        return: False"""
        if txt:
            return bool(True)
        return bool(False)
    

    def verify_pwd(self, email: str, pwd :str) -> dict:
        """Verify user password and return the user id,
        user name and user email if all of parameters is ok
        or None 
        Args:
            email (str): the user email
            pwd (str): the user password
        Returns:
            dict: {id, name, email}
            None
        """
        user = self.find_user_by_email(email)
        if user:
            if check_password_hash(user.password, str(pwd)):
                return {'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'isadm': user.isadm}
        return dict()
        

    def find_user_by_email(self, email: str) -> User | None:
        """Fynd user by email, if exist return user, if not, return None.
        Args:
            email (str): the user email
        Returns:
            str: User
            None
        """
        stmt = select(User).where(User.email == str(email)) # type: ignore
        result = db.session.execute(stmt).first()
        if result:
            user = ''
            for userr in result:
                user = userr
            if user:
                return user 
        return None