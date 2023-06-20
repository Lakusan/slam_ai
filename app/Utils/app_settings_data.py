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