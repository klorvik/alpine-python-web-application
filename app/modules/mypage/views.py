from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.modules.login.models import User
from app.modules.login.decorators import requires_login

mod = Blueprint('mypage', __name__, url_prefix='/mypage')

@mod.route('/')
@requires_login
def home():
  return render_template("mypage/home.html", user=g.user)

@mod.before_request
def before_request():
  """
  pull user's profile from the database before every request are treated
  """
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])