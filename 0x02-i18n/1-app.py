#!/usr/bin/env python3
"""Introduce bable."""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """give language options to chose based on request,"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)


def configure_babel(app):
    """Configure the app to work with bableand apply configs to it."""

    babel.init_app(app)
    app.config.from_object(Config)


# configure app
configure_babel(app)


@app.route('/')
def home():
    """domi home route."""

    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
