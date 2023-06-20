import tkinter as tk

class CameraCalib(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="Camera Calibration", font=("Arial", 18))
        label.pack(pady=20)

        button_back = tk.Button(self, text="Back to Menu", command=lambda: master.show_frame(master.main_frame))
        button_back.pack()