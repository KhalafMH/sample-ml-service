from __future__ import absolute_import, division, print_function, unicode_literals

import json
import os
import warnings

import tensorflow as tf
from flask import Flask, request, Response
from flask_cors import CORS
from tensorflow.python.util import deprecation

warnings.simplefilter(action='ignore', category=FutureWarning)
deprecation._PRINT_DEPRECATION_WARNINGS = False

app = Flask(__name__)
CORS(app)

port = None
try:
    port = os.environ['PORT']
except KeyError:
    port = "8080"

model = tf.keras.models.load_model("model/my_model.h5")


@app.route("/")
def root():
    input = request.args.get("input")
    if input is None:
        return json.dumps({"error": "No input provided"})
    prediction = model.predict([float(input)])[0][0]
    response = json.dumps({"result": str(prediction)})
    return Response(response, 200, mimetype="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
