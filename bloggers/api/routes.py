from flask import Blueprint
# from .resources.user import aaaa

bp = Blueprint("bp", __name__, url_prefix="/")
@bp.route('/', methods=['GET'])
def aaaaaa():
    return 'teste'

def init_app(app):
    app.register_blueprint(bp)
