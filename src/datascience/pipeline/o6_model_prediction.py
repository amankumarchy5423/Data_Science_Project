import joblib
import pandas as pd 
import numpy as np
from pathlib import Path


class model_prediction():
    def __init__(self):
        self.model = joblib.load(Path('models/model.pkl'))

    def predict(self, data):
        return self.model.predict(data)