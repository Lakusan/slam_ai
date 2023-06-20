import tkinter as tk
from .main_menu import MainMenu
from .camera_calib import CameraCalib
from .slam import Slam
from .settings import Settings

class FrameManager(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.title(settings.app_name)
        self.geometry("1024x768")

        self.main_frame = MainMenu(self)
        self.calib_frame = CameraCalib(self)
        self.slam_frame = Slam(self)
        self.settings_frame = Settings(self)

        self.current_frame = None

        self.show_frame(self.main_frame)

    def show_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.pack_forget()

        frame.pack()
        self.current_frame = frame
        
    def get_current_frame(self) -> tk.Frame:
        return self.current_frame