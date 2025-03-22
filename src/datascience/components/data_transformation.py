from src.datascience.entity.config_entity import data_trans_dataclass
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import os



class data_trans_action:
    def __init__(self, data : data_trans_dataclass):
        self.data = data
    
    def action_perform(self):
        data = pd.read_csv(self.data.input)

    
        # print(y.sample(5))

        train,test = train_test_split(data)
        train.to_csv(os.path.join(self.data.output,"train.csv"),index = False)
        test.to_csv(os.path.join(self.data.output,"test.csv"),index = False)
        # print(test.sample(5))
       
        