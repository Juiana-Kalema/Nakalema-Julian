import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type: ignore
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping  # type: ignore
import matplotlib.pyplot as plt
# Constants
IMAGE_SIZE = (256, 256)
BATCH_SIZE = 32
EPOCHS = 20
NUM_CLASSES = 2  # Healthy vs Diseased (for crops)
ANIMAL_CLASSES = 3  # Dog, Cat, Human (for filtering)