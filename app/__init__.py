"""
here goes all
definition of our app instance
"""

from flask import Flask, Blueprint
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

blueprint = Blueprint('project_name', __name__)
