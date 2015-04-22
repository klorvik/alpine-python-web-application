from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.modules.login.models import User
from app.modules.login.decorators import requires_login

mod = Blueprint('dashboard', __name__, url_prefix='')

@mod.route('/')
def home():
  return render_template("dashboard/home.html")