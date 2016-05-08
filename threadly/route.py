
from flask import Flask, Blueprint, request, render_template, url_for
from threadly.decor import templated
from threadly import app

import os
STATIC_HTML = os.path.dirname(__file__) + '../html/static'

threadly = Blueprint('threadly', __name__, url_prefix='/',
                     template_folder='/Users/siddharth/Workspaces/Web/mini-projects/Threadly/html',
                     static_folder=STATIC_HTML)


@threadly.route('/')
@templated('home.html')
def home():
    return {
        'html_css': url_for('threadly.static', filename='css/threadly.min.css'),
        'html_js': url_for('threadly.static', filename='js/threadly.js'),
    }