from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import joblib
import os
import pandas as pd
import numpy as np
from pathlib import Path
import mlflow
from src.datascience.utils.common import save_json
from src.datascience.entity.config_entity import model_evaluation_dataclass
from src.datascience import logger
from urllib.parse import urlparse


mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])

print("Checking MLflow authentication...")
# print(mlflow.get_experiment())  # This should work if authentication is successful


class model_evaluation_operation :
    def __init__(self, entity : model_evaluation_dataclass):
        self.entity = entity

    def operation_perform(self):
        test_data = pd.read_csv(self.entity.test_data)

        x_test_data = test_data[self.entity.x_colm]
        y_test_data = test_data[self.entity.y_colm]
        print("data is converted to pandas data frame")

        model = joblib.load(self.entity.model)
        y_predict = model.predict(x_test_data)
        print("model predict is performed")

        mse = mean_squared_error(y_true=y_test_data,y_pred=y_predict)
        mae = mean_absolute_error(y_true=y_test_data,y_pred=y_predict)
        r2 = r2_score(y_true=y_test_data,y_pred=y_predict)
        print("model evaluation metrics are calculated")

        rmse = np.sqrt(mse)

        result = {
            "mean_squared_error" : mse,
            "mean_absolute_error" : mae,
            "r2_score" : r2,
            "root_mean_squared_error" : rmse
        }
        print("saving to json   ")
        file_path = Path(self.entity.output_file)
        print(type(file_path))

        save_json(path=file_path,data=result)

        mlflow.set_registry_uri(uri= "https://dagshub.com/amankumarchy5423/Data_Science_Project.mlflow")
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            logger.info("model logged >>")
            # mlflow.sklearn.log_model(model, artifact_path=self.entity.model)

            mlflow.log_metric("mean_squared_error", mse)
            mlflow.log_metric("mean_absolute_error", mae)
            mlflow.log_metric("r2_score", r2)
            mlflow.log_metric("root_mean_squared_error", rmse)

            logger.info("all metrics loged  ")

            mlflow.models.signature.infer_signature(x_test_data,y_predict)

            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")


        

        # print(x_data.head(1))
        # print(y_data.head(1))
    