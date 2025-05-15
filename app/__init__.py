from flask import Flask, abort, request

app = Flask(__name__)
app.config["SECRET_KEY"] = 'fdgdfgdfggf786hfg6hfg6h7f'
from app import routes