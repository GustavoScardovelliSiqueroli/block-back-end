from bloggers.api.services.user_service import UserService

class UserController():
    def __init__(self, resp):
        self.resp = resp

    def register_user(self):
        
        name = self.resp['name']
        email = self.resp['email']
        pwd = self.resp['pwd']

        UserService.add_user(name, email, pwd)
        return "User registed with sucsses"
    
    