from dataclasses import dataclass
from typing import List

@dataclass
class AppSettings:
    app_name: str
    version: str
    debug_mode: bool
    theme: str
    language: str
    current_cam_index: int = None
    available_cams_index: List[int] = None
    
def get_app_name(self) -> str:
    return self.app_name

def get_version(self) -> str:
    return self.version()

def get_debug_mode(self) -> bool:
    return self.debug_mode

def get_theme(self) -> str : 
    return self.theme   

def get_language(self) -> str:
    return self.language

def get_current_cam_index(self) -> int:
    return self.current_cam_index

def get_available_cams_index(self) -> List[int]:
    return self.available_cams_index

    