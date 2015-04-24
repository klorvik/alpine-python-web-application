from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.modules.login.models import User
from app.modules.login.decorators import requires_login

mod = Blueprint('webshop', __name__, url_prefix='/webshop')

@mod.route('/')
def home():
  return render_template("webshop/tickets.html", user=g.user)

@mod.route('/tickets')
def tickets():
  return render_template("webshop/tickets.html", user=g.user)

@mod.route('/tickets/<int:id>')
def shop_tickets_item(id):
  return render_template("webshop/ticket-item/%d.html" % id, user=g.user)

@mod.route('/equipment')
def equipment():
  return render_template("webshop/equipment.html", user=g.user)

@mod.route('/equipment/<int:id>')
def shop_equipment_item(id):
  return render_template("webshop/equipment-item/%d.html" % id, user=g.user)

@mod.before_request
def before_request():
  """
  pull user's profile from the database before every request are treated
  """
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])