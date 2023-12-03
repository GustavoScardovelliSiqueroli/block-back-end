from flask import Blueprint,request
from .controllers.user_controller import UserController

user = Blueprint("user", __name__, url_prefix="/user")
@user.route('/register', methods=['POST'])
def register_user():
    resp = request.json
    user_controller = UserController(resp)
    return user_controller.register_user()


@user.route('/login', methods=['POST'])
def login_user():
    resp = request.json
    u_controller = UserController(resp)
    return u_controller.login_user()

def init_app(app):
    app.register_blueprint(user)
