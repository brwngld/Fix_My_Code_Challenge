#!/usr/bin/python3
""" Views module
"""

from flask import Blueprint

# Create the blueprint object for API version 1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the views
from api.v1.views import index
