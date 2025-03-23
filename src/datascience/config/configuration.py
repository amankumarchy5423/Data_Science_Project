from src.datascience.utils.common import load_yaml,create_directory
from src.datascience.config import *
from src.datascience.entity.config_entity import data_injection
from src.datascience.entity.config_entity import DataValidationfirst
from src.datascience.entity.config_entity import data_trans_dataclass
from src.datascience.entity.config_entity import model_train_dataclass
from src.datascience.entity.config_entity import model_evaluation_dataclass


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
    
    def DataValidation_load_yaml(self) -> DataValidationfirst :
            return DataValidationfirst(root_dir=self.loader_1.data_validation["root_dir"],
                              injuction_data_csv = self.loader_1.data_validation["injuction_data_csv"],
                              output_report = self.loader_1.data_validation["output_report"],
                              all_schema = self.loader_2.columns.input_col
                              )
        # print("all set")
        # return out


class data_trans_loadyaml:
    def __init__(
            self,
            config = CONFIG_YAML_FILE_PATH,
            param = PARAM_YAML_FILE_PATH,
            schema = SCHEMA_YAML_FILE_PATH
    ):
        self.config = load_yaml(config)
        self.param = load_yaml(param)
        self.schema = load_yaml(schema)

    def data_trans_attribute(self) -> data_trans_dataclass :
        create_directory([self.config.data_transformation['output']])
        return data_trans_dataclass (
            input = self.config.data_transformation['input'],
            output = self.config.data_transformation['output']
            
        )


class model_train_dataload:
    def __init__(self,
                 config = CONFIG_YAML_FILE_PATH,
                 params = PARAM_YAML_FILE_PATH,
                 schema = SCHEMA_YAML_FILE_PATH):
        self.config = load_yaml(config)
        self.params = load_yaml(params)
        self.schema = load_yaml(schema)
        create_directory([self.config.model_train['root_dir']])

    def model_train_entity(self) -> model_train_dataclass :
        return model_train_dataclass (
            root_dir = self.config.model_train['root_dir'],
            train_data = self.config.model_train['train_data'],
            test_data = self.config.model_train['test_data'],
            model_out = self.config.model_train['model_out'],
            alpha= self.params.ElasticNet['alpha'],
            l1_ratio=self.params.ElasticNet['l1_ratio'],
            input_col = self.schema.columns['input_col'].keys(),
            output_col = self.schema.columns["output_col"].keys()
        )

        

class model_evaluation_loadyaml:
    def __init__(self,
                 config= CONFIG_YAML_FILE_PATH,
                 params = PARAM_YAML_FILE_PATH,
                 schema =SCHEMA_YAML_FILE_PATH
                 ):
        self.config = load_yaml(config)
        self.params = load_yaml(params)
        self.schema = load_yaml(schema)

        self.temp = self.config.model_evaluation

        create_directory([self.temp['root_dir']])

    def model_evaluation_entity(self) -> model_evaluation_dataclass :
        return model_evaluation_dataclass(
            model= self.temp['model_path'],
            test_data = self.temp['test_data'],
            root_dir = self.temp['root_dir'],
            output_file = self.temp['output_file'],
            x_colm= self.schema.columns['input_col'].keys(),
            y_colm= self.schema.columns['output_col'].keys()
        )
        pass
        
        