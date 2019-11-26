from flask import Flask, jsonify, Blueprint

errorHandlers = Blueprint('Error Handlers', __name__)

@errorHandlers.app_errorhandler(404)
def handle404(description):
    print(description)
    return jsonify(error=str(description)), 404