#!/usr/bin/env python3
"""
basic hello world with Flask-Babel (v3+ API)

This module provides a minimal Flask app with Babel-based translation.
Files:
- 2-app.py      <- this file
- templates/2-index.html
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _gettext

app = Flask(__name__)


class Config(object):
    """
    Configuration values for the app.

    Attributes:
        LANGUAGES: list of supported language codes.
        BABEL_DEFAULT_LOCALE: fallback locale.
        BABEL_DEFAULT_TIMEZONE: default timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Load configuration into app BEFORE creating the Babel object.
app.config.from_object(Config)


def get_locale() -> str:
    """
    Select the best language for the current request.

    Reads the request's Accept-Language header and returns the best
    match from app.config['LANGUAGES'].
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def _(message: str) -> str:
    """
    Translate a message string.

    This function is a documented wrapper around Flask-Babel's `gettext`.
    It is provided so the symbol `_` is a real function with a docstring,
    which satisfies documentation checks and behaves the same as gettext.

    Args:
        message: The message string to translate.

    Returns:
        The translated string for the current locale.
    """
    return _gettext(message)


# Create Babel once, using the new (v3+) API: pass the selector here.
babel = Babel(app, locale_selector=get_locale)


@app.route("/", methods=['GET'])
def hello_world():
    """
    Render the main page.

    Returns the rendered template '2-index.html' with a translated greeting.
    """
    return render_template('2-index.html', greeting=_("Hello, world!"))


if __name__ == "__main__":
    # Run the app when executed directly (useful for development)
    app.run()
