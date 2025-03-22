from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
import os
from src.datascience.entity.config_entity import model_train_dataclass

class model_train_task:
    def __init__(self,data : model_train_dataclass):
        self.data = data
    
    def model_train_load(self):
        data_load = pd.read_csv(self.data.train_data)

        x_data = data_load[self.data.input_col]
        y_data = data_load[self.data.output_col]

        x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.8)

        model = ElasticNet(alpha= self.data.alpha,l1_ratio= self.data.l1_ratio)
        model.fit(x_train,y_train)

        if os.path.exists(self.data.model_out):
            os.remove(self.data.model_out)
            
        joblib.dump(model,filename= self.data.model_out)


        # print(x_train.sample(5))
        # print(y_train.columns)
        