from src.datascience import pipeline_log,logger
from src.datascience.entity.config_entity import DataValidationfirst
from src.datascience.components.data_validation import validate_column
from src.datascience.config.configuration import DataValidations_yaml_manager




class data_validation_pipeline():
    def __init__(self):
        pass

    def data_validation_pipeline_fun(self):
        try :
            pipeline_log.info("DataValidations_yaml_manager started!!")
            obj1 = DataValidations_yaml_manager()
            pipeline_log.info("DataValidations_yaml_manager ended!!")


            pipeline_log.info("datavalidaton load yam  started!!")
            temp = obj1.DataValidation_load_yaml()
            pipeline_log.info("datavalidaton load yam  ended!!")


            pipeline_log.info("validation_colum started !!!")
            obj = validate_column(temp)
            val = obj.verify_all_column()
            pipeline_log.info("validation_colum ended !!!")

        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        obj = data_validation_pipeline()
        obj.data_validation_pipeline_fun()
    except Exception as e:
        pipeline_log.exception(e)
        raise e
