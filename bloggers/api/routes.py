from flask import Blueprint,request
from .controllers.user_controller import UserController

user = Blueprint("user", __name__, url_prefix="/user")
@user.route('/register', methods=['POST'])
def aaaaaa():
    resp = request.json
    user_controller = UserController(resp)
    return user_controller.register_user()

def init_app(app):
    app.register_blueprint(user)
