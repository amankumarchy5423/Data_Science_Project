import os
import pandas as pd
from src.datascience.entity.config_entity import DataValidationfirst
from src.datascience import data_val


data_val.info("data_validation.py start >>>")

class validate_column:
    def __init__(self, config: DataValidationfirst):
        self.config = config
        print("Now in verify_all_column")

    def verify_all_column(self) -> bool:
        data = pd.read_csv(self.config.injuction_data_csv)  # Fixed KeyError
        print("File loaded....")
        
        col_repo = True  # Default to True
        try:
            data_col = list(data.columns)
            clom = self.config.all_schema.keys()
            
            for colum in data_col:
                if colum not in clom:
                    with open(self.config.output_report, mode="a") as file:  # Use 'a' to append
                        file.write(f"Column {colum} is NOT found in the schema.\n")
                    col_repo = False  # Set to False if any column is missing
                else:
                    with open(self.config.output_report, mode="a") as file:
                        file.write(f"Column {colum} is found in the schema andColumn '{colum}' contains {data[colum].isnull().sum()} null values\n")
                
                # Fixed variable reference in column check
                # with open(self.config.output_report, mode="a") as file:
                    # file.write(f"Column '{colum}' contains {data[colum].isnull().sum()} null values.\n")
                    
        except Exception as e:
            raise e
        
        return col_repo
