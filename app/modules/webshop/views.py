from flask import Blueprint, request, render_template, g, session, redirect, url_for

from app import db
from app.modules.core.models import User
from app.modules.core.models import Ticket
from app.modules.core.models import Equipment
from app.modules.login.decorators import requires_login

mod = Blueprint('webshop', __name__, url_prefix='/webshop')

@mod.route('/')
def home():
  return render_template("webshop/tickets.html", user=g.user)

@mod.route('/tickets')
def tickets():
  g.tickets = Ticket.query.all()
  return render_template("webshop/tickets.html", user=g.user, tickets=g.tickets)

@mod.route('/tickets/<int:id>')
def shop_tickets_item(id):
  g.ticket = Ticket.query.get(id)
  return render_template("webshop/ticket-item.html", user=g.user, ticket=g.ticket)

@mod.route('/equipment')
def equipment():
  g.equipment = Equipment.query.all()
  return render_template("webshop/equipment.html", user=g.user, equipment=g.equipment)

@mod.route('/equipment/<int:id>')
def shop_equipment_item(id):
  g.equipment = Equipment.query.get(id)
  return render_template("webshop/equipment-item.html", user=g.user, equipment=g.equipment)

@mod.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])
