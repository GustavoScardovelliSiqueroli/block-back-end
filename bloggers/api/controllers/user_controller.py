from bloggers.api.models.user import User
from bloggers.api.services.user_service import UserService

class UserController():
    def __init__(self, resp):
        self.resp = resp

    def register_user(self) -> dict:
        """Registers the user that was passed if all conditions are met,
          else returns the message according to the problem.
        Returns:
            dict: {message: Usuário cadastro com sucesso!}
            dict: {message: error message}
        """        
        if not 'name' in self.resp and not 'email' in self.resp and not 'pwd' in self.resp:
            return {'message': 'Todos os campos são obrigatórios!'}
        
        u_service = UserService()

        user_name = self.resp['name']

        user_pwd = self.resp['pwd']
        msg_pwd = u_service.validation_pwd(user_pwd)
        if not msg_pwd == user_pwd:
            return {'message': msg_pwd}
        
        user_email = self.resp['email']
        msg_email = u_service.validation_email(user_email)
        if not msg_email == user_email:
            return {'message': msg_email}
        
        print(u_service.find_user_by_email(user_email))

        if u_service.find_user_by_email(user_email):
            return{'message': 'Email ja registrado!'}
    
        u_service.add_user(u_service.create_user(user_name, user_email, user_pwd, isadm=self.resp.get('isadm')))
        return {'message': 'Usuário registrado com sucesso!'}
        

    def login_user(self) -> dict:
        """return the user datas if user parameters is ok
        or a message.
        Returns:
            dict: {id, email, name}
            dict: {message: error message}
        """
        if not 'email' in self.resp and not 'pwd' in self.resp:
            return {'message': 'Todos os campos são obrigatórios!'}
        
        u_service = UserService()
        resp = u_service.verify_pwd(self.resp['email'], self.resp['pwd'])
        if resp:
            return resp
        return {'message': 'Email ou senha inválidos!'}