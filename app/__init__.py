from flask import Flask

app = Flask(__name__)

from app import routes
#note that routes doesn't exist yet