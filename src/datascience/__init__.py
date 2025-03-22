import os
import logging


log_dir = "src/datascience/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir,exist_ok=True)



path = os.path.join(log_dir,"project.log")
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",filename=path)

pipeline_log = logging.getLogger("Pipeline directroy log")
utils_dir = logging.getLogger(" in utils directory")
data_val  = logging.getLogger("data_vaildation..")
logger = logging.getLogger("data_science")

# pipeline_log.error("testing errror")