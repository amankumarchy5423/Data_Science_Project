from src.datascience import logger
from src.datascience.pipeline.o1_data_ingustion import dataingustiontrain_pipeline



STAGE1 = " DATA INGUSTION "
try :
  logger.info(f" starting the process {STAGE1} >>>>")
  obj = dataingustiontrain_pipeline()
  obj.igniciate()
  logger.info(f"completed {STAGE1} >>>>")
except Exception as e :
  logger.exception(e)
  raise e