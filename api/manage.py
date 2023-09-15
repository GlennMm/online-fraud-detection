#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import tensorflow as tf
from tensorflow.keras import activations, regularizers
from tensorflow.keras.layers import Activation, Dense, Dropout, BatchNormalization

from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

from tensorflow.python.keras.layers import deserialize, serialize
from tensorflow.python.keras.saving import saving_utils
from tensorflow.keras.models import Model

def unpack(model, training_config, weights):
    restored_model = deserialize(model)
    if training_config is not None:
        restored_model.compile(
            **saving_utils.compile_args_from_training_config(
                training_config
            )
        )
    restored_model.set_weights(weights)
    return restored_model

# Hotfix function
def make_keras_picklable():

    def __reduce__(self):
        model_metadata = saving_utils.model_metadata(self)
        training_config = model_metadata.get("training_config", None)
        model = serialize(self)
        weights = self.get_weights()
        return (unpack, (model, training_config, weights))

    cls = Model
    cls.__reduce__ = __reduce__


def get_neural_network():    
    l1=0.0000001
    l2=0.0000001
    dropout=0.05
    epochs = 100
    
    model = Sequential()
    model.add(Dense(100, activation=activations.linear, input_shape = (431,), activity_regularizer=regularizers.l1(l1), kernel_regularizer=regularizers.l2(l2)))
    model.add(Activation(activation=activations.relu))

    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(100, activation=activations.linear, activity_regularizer=regularizers.l1(l1), kernel_regularizer=regularizers.l2(l2)))
    model.add(Activation(activation=activations.relu))

    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(100, activation=activations.linear, activity_regularizer=regularizers.l1(l1), kernel_regularizer=regularizers.l2(l2)))
    model.add(Activation(activation=activations.relu))


    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(50, activation=activations.linear, activity_regularizer=regularizers.l1(l1), kernel_regularizer=regularizers.l2(l2)))
    model.add(Activation(activation=activations.relu))

    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(1, activation=activations.sigmoid))

    model.compile(optimizer=Adam(), loss=tf.keras.losses.logcosh, metrics=['accuracy'])

    return model


def main():
    """Run administrative tasks."""
    make_keras_picklable()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
