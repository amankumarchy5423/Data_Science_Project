from dataclasses import dataclass
from pathlib import Path

@dataclass
class data_injection :
    root_dir : Path
    source_url :str
    output_zip :Path
    output : Path
