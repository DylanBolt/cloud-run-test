from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import logging
import json
import requests
import cloudpickle
import pickle

#Intialize the flask app
app = Flask(__name__)


#Custom error handler
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

model = cloudpickle.dumps('phish-model-1649995335.cloudpickle')



@app.route('/predict', methods = ['POST'])
def predict():
    """This route returns a predictions in JSON."""
    predictions = model.predict()
    return jsonify('pong!')
