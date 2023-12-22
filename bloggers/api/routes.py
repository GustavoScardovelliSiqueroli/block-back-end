from flask import Blueprint,request
from .controllers.user_controller import UserController
from .controllers.posts_controller import PostController
from .controllers.post_contents_controller import PostContentsController
from bloggers.ext.cors import cross_origin

user = Blueprint('user', __name__, url_prefix='/user')
posts = Blueprint('posts', __name__, url_prefix='/posts')
postcontents = Blueprint('postcontents', __name__, url_prefix='/posts/contents')

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
@cross_origin()
def register_post():
    pst_controller = PostController(request.json)   
    return pst_controller.register_post() 

@posts.route('/', methods=['GET'])
@cross_origin()
def get_posts():
    pst_controller = PostController('')
    return pst_controller.get_posts()

# ROUTE - POSTS/CONTENTS
@postcontents.route('/teste', methods=['GET'])
@cross_origin()
def teste():
    pst_cntnts_controller = PostContentsController('teste')
    return pst_cntnts_controller.teste()

@postcontents.route('delete', methods=['GET'])
@cross_origin()
def delete_content():
    pst_cntnts_controller = PostContentsController('teste')
    return pst_cntnts_controller.delete_post_content()

def init_app(app):
    app.register_blueprint(user)
    app.register_blueprint(posts)
    app.register_blueprint(postcontents)
