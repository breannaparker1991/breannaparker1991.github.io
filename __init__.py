from flask import Flask
from gitignore.env import KEY

app = Flask(__name__)
app.secret_key = KEY