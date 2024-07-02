from dataclasses import dataclass
from pathlib import Path

@dataclass
class Dataingestionconfig:
    root_dir:Path
    source_name: str
    local_file: Path

    
@dataclass
class Datatransformationconfig:
    root_dir:Path
    source_name: str
    local_file: str
    transformed_path: Path
    