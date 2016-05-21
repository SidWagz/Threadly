
from flask import Flask, Blueprint, request, render_template, url_for, jsonify
from threadly.decor import templated
from threadly import app
import os

HTML_TEMPLATES = '/'.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'html'))

threadly = Blueprint('threadly', __name__,
                     template_folder=HTML_TEMPLATES)

@threadly.route('/', methods=['GET'])
@templated('home.html')
def home():
    if request.method == 'GET':

        # @DEBUG : debug all routes registered
        # links = []
        # for rule in app.url_map.iter_rules():
        #     links.append(rule.rule)
        #
        # print('-----------------------')
        # for link in links:
        #     print(link)
        # print('-----------------------')

        return {}

@threadly.route('/_post_comment', methods=['POST'])
def post_comment():
    if request.method == 'POST':

        values = {}

        return jsonify(**values)
