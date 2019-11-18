from flask import Flask
from flask import render_template
from flask import request

import os

app = Flask(__name__)


@app.route("/")
def landing_page():
    context = {'project': "Flask Player", 'author': "Yajun Zhao",
               'items': ["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"]}
    return render_template('landing_page.html', **context)


@app.route("/home")
def get_home():
    context = {'project': "Flask Player", 'author': "Yajun Zhao",
               'items': ["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"]}
    return render_template('home.html', **context)


@app.route("/about")
def get_about():
    context = {'project': "Flask Player", 'author': "Yajun Zhao",
               'items': ["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"]}
    return render_template('about.html', **context)


@app.route("/contact")
def get_contact():
    context = {'project': "Flask Player", 'author': "Yajun Zhao",
               'items': ["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"]}
    return render_template('contact.html', **context)


@app.route("/privacy")
def get_privacy():
    context = {'project': "Flask Player", 'author': "Yajun Zhao",
               'items': ["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"]}
    return render_template('privacy.html', **context)


if __name__ == '__main__':
    app.debug = False
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
