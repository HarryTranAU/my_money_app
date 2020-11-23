from dotenv import load_dotenv
from flask import Flask, jsonify
from database import init_db

load_dotenv()
app = Flask(__name__)
app.config.from_object("settings.app_config")
db = init_db(app)

from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)

from marshmallow.exceptions import ValidationError

@app.errorhandler(ValidationError)
def handle_bad_request(error):
    return(jsonify(error.messages), 400)
