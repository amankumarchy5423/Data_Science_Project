from src.datascience.utils.common import load_yaml,create_directory
from src.datascience.config import *
from src.datascience.entity.config_entity import data_injection
from src.datascience.entity.config_entity import DataValidationfirst


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
    
class DataValidations_yaml_manager :
    def __init__(self,
            config = CONFIG_YAML_FILE_PATH,
            params = PARAM_YAML_FILE_PATH,
            schema = SCHEMA_YAML_FILE_PATH
    ):
        self.config = config
        self.params = params
        self.schema = schema
        
        self.loader_1 = load_yaml(self.config)
        self.loader_2 = load_yaml(self.schema)

        print("file loaded successfully")


        create_directory([self.loader_1.data_validation["root_dir"]])
    # def DataValidation_load_yaml(self) -> DataValidationfirst:
    #     # loader = self.loader_1
    #     print("now the termpoint")
    #     out = DataValidationfirst(
    #         root_dir=self.loader_1.data_validation["root_dir"],
    #         injuction_data_csv = self.loader_1.data_validation["injuction_data_csv"],
    #         output_report = self.loader_1.data_validation["output_report"],
    #         all_schema = self.loader_2.columns.input_col
            # root_dir=loader.data_validation['root_dir'],
            # injuction_data_csv = loader.data_validation['injusion_data_csv'],
            # output_report = loader.data_validation['output_report'],
            # all_schema = self.loder_2.columns['input_col']

        # )
    def DataValidation_load_yaml(self) -> DataValidationfirst :
            return DataValidationfirst(root_dir=self.loader_1.data_validation["root_dir"],
                              injuction_data_csv = self.loader_1.data_validation["injuction_data_csv"],
                              output_report = self.loader_1.data_validation["output_report"],
                              all_schema = self.loader_2.columns.input_col
                              )
        # print("all set")
        # return out
