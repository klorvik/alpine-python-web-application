import os
import sys

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import modules
from app.modules.dashboard.views import mod as dashboardModule
app.register_blueprint(dashboardModule)

from app.modules.login.views import mod as loginModule
app.register_blueprint(loginModule)

from app.modules.webshop.views import mod as webshopModule
app.register_blueprint(webshopModule)

from app.modules.mypage.views import mod as mypageModule
app.register_blueprint(mypageModule)

from app.modules.contact.views import mod as contactModule
app.register_blueprint(contactModule)

#Add dummydata
from app.modules.core.models import User
from app.modules.core.models import Ticket

ticket1 = Ticket(name='Nybegynner', price=300, description='Asdasd', imageurl='http://placehold.it/800x300')
ticket2 = Ticket(name='Medium', price=500, description='Asdasd', imageurl='http://placehold.it/800x300')
ticket3 = Ticket(name='Ekspert', price=800, description='Asdasd', imageurl='http://placehold.it/800x300')
# Insert the record in our database and commit it
db.session.add(ticket1)
db.session.add(ticket2)
db.session.add(ticket3)
db.session.commit()
