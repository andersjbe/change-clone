import os
from flask import Flask, render_template, request, session
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from app.models import db, User
from app.api.api import user_routes, petition_routes, update_routes, topic_routes
from app.config import Config

app = Flask(__name__, static_url_path='')

app.config.from_object(Config)
app.register_blueprint(petition_routes, url_prefix='/api/petitions')
app.register_blueprint(update_routes, url_prefix='/api/updates')
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(topic_routes, url_prefix='/api/topics')
db.init_app(app)
jwt = JWTManager(app)
Migrate(app, db, compare_type=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['FLASKS3_BUCKET_NAME'] = ''


# Application Security
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def inject_csrf_token(response):
    response.set_cookie('csrf_token',
                        generate_csrf(),
                        secure=True if os.environ.get('FLASK_ENV') else False,
                        samesite='Strict' if os.environ.get(
                            'FLASK_ENV') else None,
                        httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path>')
def react_root(path):
    return app.send_static_file('index.html')
