import tkinter as tk
from tkinter import ttk
import threading
import time
from ..Utils.cam_manager import CameraManager

class LoadingScreen(tk.Frame):
    def __init__(self, master): 
        super().__init__(master)
        self.master = master
        self.camera_manager = CameraManager()
        self.create_widgets()
        self.start_loading()
        
    def create_widgets(self):
        self.loading_label = tk.Label(self, text="Loading...")
        self.loading_label.pack(pady=20)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=10)
    
    def start_loading(self):
        self.thread = threading.Thread(target=self.run_tasks)
        self.thread.start()
        
    def run_tasks(self):
        # find all active usb cameras
        self.loading_label.config(text="Looking for USB Web Cams")
        try:
            self.camera_manager.find_available_cameras()
        except Exception as e:
            self.loading_label.config(text="No USB-Camera found. Please connect one and restart the app.")

        cameras_found = "Found " + str(len(self.camera_manager.get_availabe_cameras())) + " Camera(s)"
        self.loading_label.config(text=cameras_found)
        time.sleep(2)
        self.loading_label.config(text="Stuff Loaded! Redirecting to Main Menu...")
        time.sleep(2)
        self.master.show_frame(self.master.main_frame)
        
    # for starting the next thread -> not needed right now
    def update_progress(self):
        if self.thread.is_alive():
            # 100 is the delay in ms until tkinter does the next step
            print("update progress")
            self.master.after(100, self.update_progress)
        else:
            pass
            