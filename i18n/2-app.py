#!/usr/bin/env python3
"""
basic hello world example
"""
import flask
from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext as _
app = Flask(__name__)


class Config(object):
    """
    a configuration values for the flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale() -> str:
    """Select a language translation to use for that request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def hello_world():
    """renders the main page"""
    # Use a template; translation function available as _ in Jinja too
    return render_template('2-index.html', greeting=_("Hello, world!"))


if __name__ == "__main__":
    # Run the app when executed directly (useful for development)
    app.run()
