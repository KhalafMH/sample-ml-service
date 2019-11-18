from __future__ import absolute_import, division, print_function, unicode_literals

import json
import os
import warnings

import tensorflow as tf
from flask import Flask, request
from tensorflow.python.util import deprecation

warnings.simplefilter(action='ignore', category=FutureWarning)
deprecation._PRINT_DEPRECATION_WARNINGS = False

app = Flask(__name__)

model = tf.keras.models.load_model("model/my_model.h5")


@app.route("/")
def root():
    input = request.args.get("input")
    if input is None:
        return json.dumps({"error": "No input provided"})
    prediction = model.predict([float(input)])
    return json.dumps({"result": str(prediction)})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ['PORT'])
