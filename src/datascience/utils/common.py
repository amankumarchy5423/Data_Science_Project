from src.datascience import utils_dir
import yaml
import os
import joblib
import json
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from typing import Any



@ensure_annotations
def create_directory(path : list):
    utils_dir.info("creating directory")
    for directory in path:
        os.makedirs(directory, exist_ok=True)
    utils_dir.info("path is created")

@ensure_annotations
def load_yaml(path : Path) -> dict:
    utils_dir.info("loading yaml file")
    try :
       with open(path, 'r') as file:
         yml_file = yaml.safe_load(file)
       return ConfigBox(yml_file)
    except Exception as e:
        utils_dir.error("yaml file is not found")
        raise e
    
@ensure_annotations
def save_json(path : Path , data : dict) :
    utils_dir.info("saving json file")
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        utils_dir.info(f"json file is saved at : {path}")

@ensure_annotations
def load_json(path : Path,data: dict):
    utils_dir.info("loading json file")
    try :
        with open(path, 'r') as f:
            data = json.load(f)
            return ConfigBox(data)
    except Exception as e:
        raise e

@ensure_annotations
def save_model(path : Path , model: Any):
    utils_dir.info("saving ml_model file")
    try :
        with open(path) as o:
            joblib.dump(model, o)
    except Exception as e:
        raise e

@ensure_annotations
def load_model(pathn : Path):
    utils_dir.info("loading loading ml_lodel")
    try :
        with open(pathn) as o:
            model = joblib.load(o)
            return model
    except Exception as e:
        raise e


        


# utils_dir.error("test error")