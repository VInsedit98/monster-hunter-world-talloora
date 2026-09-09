# build ac39d31181
# (auto) e8bd7e
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
