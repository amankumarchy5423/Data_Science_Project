from src.datascience import pipeline_log
from src.datascience.config.configuration import data_trans_loadyaml
from src.datascience.components.data_transformation import data_trans_action





class data_trans_pipeline:
    def __init__(self):
        pipeline_log.info ("Data Transformation Pipeline Started")
        pass

    def data_trans_pipeline_fun(self):

        pipeline_log.info("data trans load yaml started>>>")
        obj = data_trans_loadyaml()
        pipeline_log.info("data trans load yaml ended>>>")

        pipeline_log.info("data_trans attributr started>>>")
        temp = obj.data_trans_attribute()
        pipeline_log.info("data_trans attributr ended>>>")

        pipeline_log.info ("data_trans action started>>>")
        obj2 = data_trans_action(temp)
        obj2.action_perform()
        pipeline_log.info ("data_trans action ended>>>")


if __name__ == "__main__":
    try :
        obj = data_trans_pipeline()
        obj.data_trans_pipeline_fun()
    except Exception as e:
        pipeline_log.error("Error in data_trans_pipeline: %s" % str(e))
        raise e