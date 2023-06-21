import cv2
from typing import List

class CameraManager():
    
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
            return False
    
    def get_availabe_cameras(self) -> List[int]:
        return self.cameras
        
    
    def get_camera_index(self) -> int:
        return self.cameraIndex