import cv2
from typing import List

class CameraManager:
    _instance = None
    
    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def __init__(self):
        self.cameras = []
        self.cameraIndex = None
        
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ()
        return cls._instance

    @classmethod
    def find_available_cameras(self) -> bool:
        self.cameras = []
        index = 0
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            self.cameras.append(index)
            cap.release()
            index += 1
        if len(self.cameras) != 0:
                return True
        else:
            raise Exception("No cameras found")

    @classmethod
    def get_available_cameras(self) -> List[int]:
        return self.cameras
    
    @classmethod
    def get_camera_index(self) -> int:
        return self.cameraIndex