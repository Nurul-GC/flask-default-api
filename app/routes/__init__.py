"""defining our routes"""

from app import blueprint
from flask import render_template, request, jsonify


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form['value_name']
        return jsonify(key_name=value)
    return render_template("index.html")
