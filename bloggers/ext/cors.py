from flask_cors import  CORS, cross_origin

cors = CORS()

def init_app(app):
    cors.init_app(app)