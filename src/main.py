from dotenv import load_dotenv
from flask import Flask
from controllers import registerable_controllers

load_dotenv()
app = Flask(__name__)
for controller in registerable_controllers:
    app.register_blueprint(controller)
