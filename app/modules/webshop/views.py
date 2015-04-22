from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
#from app.modules.dashboard.models import User
from app.modules.dashboard.decorators import requires_login

mod = Blueprint('webshop', __name__, url_prefix='/webshop')

@mod.route('/')
@requires_login
def home():
  return render_template("webshop/home.html", user=g.user)