import tkinter as tk
from tkinter import ttk


class Settings(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        label = tk.Label(self, text="Settings", font=("Arial", 18))
        label.pack(pady=20)

        self.button_back = tk.Button(self, text="Back to Menu", command=lambda: master.show_frame(master.main_frame))
        self.button_identify_cams = tk.Button(self, text="Indentify Cams", command=lambda: self.select_current_cam())
        
        self.button_back.pack()
        self.button_identify_cams.pack()
        
        self.camera_var = "title"
        self.available_cameras =[1,2,3]
        self.camera_dropdown = ttk.Combobox(self, textvariable=self.camera_var, values=self.available_cameras)
        self.camera_dropdown.pack()
        
    def select_current_cam(self):
        print("Camera selected")
    
    def populate_dopdown():
        pass
        