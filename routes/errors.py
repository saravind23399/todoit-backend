from flask import Flask, jsonify, Blueprint

errorHandlers = Blueprint('Error Handlers', __name__)

@errorHandlers.app_errorhandler(404)
def handle404(description):
    return jsonify(error=str(description)), 404

@errorHandlers.app_errorhandler(400)
def handle400(description):
    return jsonify(error=str(description)), 400