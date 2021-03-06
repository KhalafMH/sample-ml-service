from __future__ import absolute_import, division, print_function, unicode_literals

import os
import warnings

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.util import deprecation

warnings.simplefilter(action='ignore', category=FutureWarning)
deprecation._PRINT_DEPRECATION_WARNINGS = False


def create_model():
    xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs, ys, epochs=500)

    return model


if __name__ == "__main__":
    model = create_model()
    print(model.predict([10.0]))
    model_save_location = "model"
    os.makedirs(model_save_location, exist_ok=True)
    model.save("model/my_model.h5")
