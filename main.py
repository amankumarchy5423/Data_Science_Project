from src.datascience import logger
from src.datascience.pipeline.o1_data_ingustion import dataingustiontrain_pipeline
from src.datascience.pipeline.o2_data_validation import data_validation_pipeline



STAGE1 = " DATA INGUSTION "
try :
  logger.info(f" starting the process {STAGE1} >>>>")
  obj = dataingustiontrain_pipeline()
  obj.igniciate()
  logger.info(f"completed {STAGE1} >>>>")
except Exception as e :
  logger.exception(e)
  raise e

STAGE2 = " DATA VALIDATION "
try :
  logger.info(f" starting the process {STAGE2} >>>>")
  obj2 = data_validation_pipeline()
  obj2.data_validation_pipeline_fun()
  logger.info(f"completed {STAGE2} >>>>")
except Exception as e :
  logger.exception(e)
  raise e

