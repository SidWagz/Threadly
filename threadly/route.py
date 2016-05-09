
from flask import Flask, Blueprint, request, render_template, url_for
from threadly.decor import templated
from threadly import app

import os
HTML_TEMPLATES = '/'.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'html'))

threadly = Blueprint('threadly', __name__, url_prefix='/',
                     template_folder=HTML_TEMPLATES)

@threadly.route('/')
@templated('home.html')
def home():
    return {}