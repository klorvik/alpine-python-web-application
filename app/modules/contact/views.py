from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.modules.core.models import User

mod = Blueprint('contact', __name__, url_prefix='/contact')

@mod.before_request
def before_request():
  """
  pull user's profile from the database before every request are treated
  """
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/')
def home():
  return render_template("contact/home.html", user=g.user)
