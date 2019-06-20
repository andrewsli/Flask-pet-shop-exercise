"""Flask application for a pet store: can view and add pets."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from db import Pet

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

toolbar = DebugToolbarExtension(app)

