from flask import render_template, session, redirect, url_for, flash
from . import main
#from .forms import ...
from .. import db
#from ..models import ...
from .utils import *

@main.route('/')
def index():
    return render_template("index.html")