import os
import sys

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# Create DB if it doesn't exist
if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    db.create_all()

def install_secret_key(app, filename='secret_key'):
    filename = os.path.join(app.instance_path, filename)

    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.isdir(full_path):
            print('mkdir -p {filename}'.format(filename=full_path))
        print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
        sys.exit(1)

if not app.config['DEBUG']:
    install_secret_key(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.modules.dashboard.views import mod as dashboardModule
app.register_blueprint(dashboardModule)

from app.modules.login.views import mod as loginModule
app.register_blueprint(loginModule)

from app.modules.webshop.views import mod as webshopModule
app.register_blueprint(webshopModule)

from app.modules.mypage.views import mod as mypageModule
app.register_blueprint(mypageModule)