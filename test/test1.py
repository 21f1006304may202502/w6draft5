"""
import pytest
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import accuracy_score
"""
import os

# Load the model
current_dir = os.path.dirname(os.path.abspath(__file__))
train_dir = os.path.abspath(os.path.join(current_dir,"..","train"))
print(train_dir)
