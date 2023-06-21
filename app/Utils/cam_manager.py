import cv2
from typing import List

class CameraManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.cameras = []
        self.cameraIndex = None

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

    def get_available_cameras(self) -> List[int]:
        return self.cameras
    
    def get_camera_index(self) -> int:
        return self.cameraIndex