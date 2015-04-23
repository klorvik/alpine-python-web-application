from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

mod = Blueprint('contact', __name__, url_prefix='/contact')

@mod.route('/')
def home():
  return render_template("contact/home.html")

