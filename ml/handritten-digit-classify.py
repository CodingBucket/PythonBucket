# This program classifies the handritten number 0 - 9

# pip install tensorflow keras numpy mnist matplotlib

import numpy as np
import mnist # Get data set
import matplotlib.pyplot as plt # Graph
from keras.models import Sequential # ANN architecture
from keras.layers import Dense # The layers in the ANN
from keres.util import to_categorical

# Load the data set
train_images = mnist.train_images() # Training data images
