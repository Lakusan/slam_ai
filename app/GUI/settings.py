import tkinter as tk
from tkinter import ttk
from ..Utils.cam_manager import CameraManager
from ..Utils.app_settings_data import AppSettings
from typing import List



class Settings(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        label = tk.Label(self, text="Settings", font=("Arial", 18))
        label.pack(pady=20)

        self.button_back = tk.Button(self, text="Back to Menu", command=lambda: master.show_frame(master.main_frame))
        self.button_identify_cams = tk.Button(self, text="Indentify Cams", command=lambda: self.select_current_cam())
        
        self.button_back.pack()
        self.button_identify_cams.pack()
        
        # camera manager
        self.camera_var = "title"
        self.camera_manager = CameraManager()
        self.available_cameras = []
        self.available_cameras.append("None")
        # drop down menu to select the camera index
        self.camera_dropdown = ttk.Combobox(self, textvariable=self.camera_var, values=self.available_cameras)
        self.camera_dropdown.pack()
        # bind event on dropdown -> mouse enters -> get data
        self.camera_dropdown.bind('<Enter>', self.populate_dropdown)
        # bind event on dropdown -> on Selection -> set cam_index on AppSettings
        self.camera_dropdown.bind('<<ComboboxSelected>>', self.handle_selection)
        
        
        # App Settings Instance (dataclass) to store selected Camera if not cam_index=0
        self.app_settings = AppSettings.get_instance()
        
    def select_current_cam(self):
        print("Camera selected")
    
    def populate_dropdown(self, event):
        self.camera_dropdown['values'] = self.camera_manager.get_available_cameras()
            
    def handle_selection(self, event):
        self.app_settings.set_current_cam_index(self.camera_dropdown.get())
        