import os
from urllib import request 
import zipfile
from src.datascience.entity.config_entity import data_injection


class Dataingestion():
    def __init__(self, data : data_injection):
        self.data = data
    
    def download_file(self):
        if not os.path.exists(self.data.output_zip):
            os.makedirs(self.data.root_dir,exist_ok=True)
            filename,headers = request.urlretrieve(
                self.data.source_url, self.data.output_zip)
        else :
            print("File already exists")

    def unzip_file(self):
        output_file = self.data.output
        os.makedirs(output_file,exist_ok=True)
        with zipfile.ZipFile(self.data.output_zip, 'r') as zip_ref:
            zip_ref.extractall(output_file)

            