import tkinter as tk

class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="Main Menu", font=("Arial", 18))
        label.pack(pady=20)

        button_calib = tk.Button(self, text="Camera Calibration", command=lambda: master.show_frame(master.calib_frame))
        button_slam = tk.Button(self, text="SLAM", command=lambda: master.show_frame(master.slam_frame))
        button_settings = tk.Button(self, text="Settings", command=lambda: master.show_frame(master.settings_frame))
        button_calib.pack()
        button_slam.pack()
        button_settings.pack()