#!/usr/bin/env python3
"""
basic hello world example
"""
import flask
from flask import Flask, render_template, g, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    a configuration variable
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale() -> str:
    """Select a language translation to use for that request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])



app.config.from_object(Config)


@app.route("/", methods=['GET'])
def hello_world():
    """hello world"""
    return render_template('2-index.html')
