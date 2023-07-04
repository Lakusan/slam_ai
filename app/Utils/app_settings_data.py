from dataclasses import dataclass
from typing import List

@dataclass
class AppSettings:

    app_name: str
    version: str
    debug_mode: bool
    theme: str
    language: str
    window_size: str
    current_cam_index: int = 0
    available_cams_index: List[int] = None
    calib_img_path: str = "calibration_images"
    calib_params_path: str = "calib_params"
    
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = AppSettings(app_name="Simple Mono-SLAM", version="0.1", debug_mode=True, theme="Light", language="English", window_size="1024x768")
        return cls._instance
    
    @classmethod
    def get_app_name(self) -> str:
        return self.app_name
    
    @classmethod
    def get_version(self) -> str:
        return self.version()

    @classmethod
    def get_debug_mode(self) -> bool:
        return self.debug_mode

    @classmethod
    def get_theme(self) -> str : 
        return self.theme   

    @classmethod
    def get_language(self) -> str:
        return self.language

    @classmethod
    def get_current_cam_index(self) -> int:
        return self.current_cam_index
    
    @classmethod
    def set_current_cam_index(self, index):
        self.current_cam_index = index

    @classmethod
    def get_available_cams_index(self) -> List[int]:
        return self.available_cams_index
    
    @classmethod
    def get_window_size(self) -> str:
        return self.window_size
    
    @classmethod
    def get_calib_img_path(self) -> str:
        return self.calib_img_path
    
    @classmethod
    def get_calib_params_path(self) -> str:
        return self.calib_params_path