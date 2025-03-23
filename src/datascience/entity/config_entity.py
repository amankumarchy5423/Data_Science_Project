from dataclasses import dataclass
from pathlib import Path

@dataclass
class data_injection :
    root_dir : Path
    source_url :str
    output_zip :Path
    output : Path



@dataclass
class DataValidationfirst():
    root_dir : Path
    injuction_data_csv : Path
    output_report : Path
    all_schema : dict

@dataclass
class data_trans_dataclass:
    input : Path
    output : Path
   
@dataclass
class model_train_dataclass:
    root_dir : str
    train_data : Path
    test_data : Path
    model_out : Path
    alpha : float
    l1_ratio : float
    input_col : None
    output_col :None


@dataclass
class model_evaluation_dataclass :
    model : Path
    test_data : Path
    root_dir : Path
    output_file : Path
    x_colm : None
    y_colm : None