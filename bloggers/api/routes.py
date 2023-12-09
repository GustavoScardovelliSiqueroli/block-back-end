from flask import Blueprint,request
from .controllers.user_controller import UserController
from .controllers.posts_controller import PostController
from bloggers.ext.cors import cross_origin

user = Blueprint('user', __name__, url_prefix='/user')
posts = Blueprint('posts', __name__, url_prefix='/posts')

# ROUTE - USER
@user.route('/register', methods=['POST'])
@cross_origin()
def register_user():
    user_controller = UserController(request.json)
    return user_controller.register_user()


@user.route('/login', methods=['POST'])
@cross_origin()
def login_user():
    resp = request.json
    u_controller = UserController(resp)
    return u_controller.login_user()

    
# ROUTE - POSTS
@posts.route('/register', methods=['POST'])
def register_post():
    pst_controller = PostController(request.json)   
    return pst_controller.register_post() 

def init_app(app):
    app.register_blueprint(user)
    app.register_blueprint(posts)
