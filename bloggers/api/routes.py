from re import escape
from flask import Blueprint,request

from bloggers.api.controllers.comments_controller import CommentsController
from .controllers.user_controller import UserController
from .controllers.posts_controller import PostController
from .controllers.post_contents_controller import PostContentsController
from bloggers.ext.cors import cross_origin

user = Blueprint('user', __name__, url_prefix='/user')
posts = Blueprint('posts', __name__, url_prefix='/posts')
postcontents = Blueprint('postcontents', __name__, url_prefix='/posts/contents')
comments = Blueprint('comments', __name__, url_prefix='/comments')

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

@posts.route('/<idpost>', methods=['DELETE'])
@cross_origin()
def delete_post(idpost):
    req = {'idpost': idpost}
    pst_controller = PostController(req)
    return pst_controller.delete_post()

@posts.route('/<idpost>', methods=['GET'])
@cross_origin()
def get_post(idpost):
    req = {'idpost': idpost}
    pst_controller = PostController(req)
    return pst_controller.get_post()

# ROUTE - POSTS/CONTENTS
@postcontents.route('/delete', methods=['GET'])
@cross_origin()
def delete_content():
    pst_cntnts_controller = PostContentsController('teste')
    return pst_cntnts_controller.delete_post_content()

@postcontents.route('/teste/<teste>', methods=['GET'])
def teste(teste):
    return f'teste: {escape(teste)}'

# ROUTE - COMMENTS
@comments.route('/register', methods=['POST'])
@cross_origin()
def register_comments():
    cmnts_controller = CommentsController(request.json)
    return cmnts_controller.register_comments()

@comments.route('/<idcomment>', methods=['DELETE'])
@cross_origin()
def delete_comment(idcomment):
    req = {'idcomment': idcomment}
    cmnts_controller = CommentsController(req)
    return cmnts_controller.delete_comment()

@comments.route('/',methods=['GET'])
@cross_origin()
def testesegund():
    cmnts_controller = CommentsController('teste')
    return cmnts_controller.update_comments()


def init_app(app):
    app.register_blueprint(user)
    app.register_blueprint(posts)
    app.register_blueprint(postcontents)
    app.register_blueprint(comments)
