from src.datascience import pipeline_log
from src.datascience.components.model_evaluation import model_evaluation_operation
from src.datascience.config.configuration import model_evaluation_loadyaml



class modelevaluation_pipeline :
    def __init__(self):
        pass

    def modelevaluation_pipeline_fun(self):

        pipeline_log.info("model_evaluation load yaml start >>>")
        obj = model_evaluation_loadyaml()
        pipeline_log.info("model_evaluation load yaml end >>>")

        pipeline_log.info("model evaluation operation start >>>")
        temp = obj.model_evaluation_entity()
        pipeline_log.info("model evaluation operation end >>>")

        pipeline_log.info("model_evaluation operation start >>>")
        obj2 = model_evaluation_operation(temp)
        obj2.operation_perform()
        pipeline_log.info("model_evaluation operation end >>>")