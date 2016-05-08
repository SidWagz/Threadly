
from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404_error.html'), 404

from threadly.route import threadly as threadly_module

app.register_blueprint(threadly_module)