from __future__ import absolute_import, division, print_function, unicode_literals

import warnings

import tensorflow as tf
from tensorflow.python.util import deprecation

warnings.simplefilter(action='ignore', category=FutureWarning)
deprecation._PRINT_DEPRECATION_WARNINGS = False

if __name__ == '__main__':
    model = tf.keras.models.load_model("model/my_model.h5")
    print(model.predict([10.0]))
