from src.datascience.utils.common import load_yaml,create_directory
from src.datascience.config import *
from src.datascience.entity.config_entity import data_injection

class data_manager():
    def __init__(self,
            config_filepath=CONFIG_YAML_FILE_PATH,
            prams_filepath = PARAM_YAML_FILE_PATH,
            schema_filepath = SCHEMA_YAML_FILE_PATH
    ):
        self.config = load_yaml(config_filepath)
        self.prams = load_yaml(prams_filepath)
        self.schema = load_yaml(schema_filepath)

        create_directory([self.config.data_root])

    def data_injection_fun(self) -> data_injection :
        return data_injection(root_dir=self.config.data_injuction["root_dir"],
                              source_url=self.config.data_injuction["source_url"],
                              output_zip=self.config.data_injuction["output_zip"],
                              output=self.config.data_injuction["output"]
                              )
