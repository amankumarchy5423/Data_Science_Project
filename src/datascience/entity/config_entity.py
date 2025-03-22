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
   