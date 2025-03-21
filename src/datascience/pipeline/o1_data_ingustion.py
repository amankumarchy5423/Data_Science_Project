from src.datascience.entity.config_entity import data_injection
from src.datascience.config.configuration import data_manager
from src.datascience.components.data_ingustion import Dataingestion
from src.datascience import pipeline_log

class dataingustiontrain_pipeline:
    def __init__(self):
        pass

    def igniciate(self):
        injustion = data_manager()

        pipeline_log.info("data_manager is run successfully ")

        opt = injustion.data_injection_fun()
        
        opt2 = Dataingestion(opt)

        pipeline_log.info("Dataingestion is run successfully ")

        opt2.download_file()

        pipeline_log.info("file downloaded ")

        opt2.unzip_file()

        pipeline_log.info("all the task perform succes full  ")


if __name__ == "__main__":
    try :
      obj = dataingustiontrain_pipeline()
      obj.igniciate()
    except Exception as e :
        raise e