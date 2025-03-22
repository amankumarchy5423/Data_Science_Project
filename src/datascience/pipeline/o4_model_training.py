from src.datascience.config.configuration import model_train_dataload
from src.datascience.components.model_training import * 
from src.datascience import pipeline_log


class ModelTraining_pipeline:
    def __init__(self):
        pass

    def modeltraining_pipline_fun(self):

        pipeline_log.info("model trainig dataload start >>>")
        obj = model_train_dataload()
        pipeline_log.info("model trainig dataload end >>>")

        pipeline_log.info("model train entity started >>>")
        temp = obj.model_train_entity()
        pipeline_log.info("model train entity ended >>>")

        pipeline_log.info("model training started >>>")
        obj2 = model_train_task(temp)
        obj2.model_train_load()
        pipeline_log.info("model training endeed >>>")



if __name__ == "__main__":
    try :
        obj = ModelTraining_pipeline()
        obj.modeltraining_pipline_fun()
    except Exception as e:
        pipeline_log.exception(e)
        raise e
