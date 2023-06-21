import tkinter as tk
from tkinter import ttk
import threading
import time

class LoadingScreen(tk.Frame):
    def __init__(self, master): 
        super().__init__(master)
        self.master = master
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
        self.super_method()
        self.progress_var.set(50)
        self.super_method()
        self.progress_var.set(100)
        self.update_progress()
    
    def super_method(self):
        time.sleep(1)
        print("done")
        self.master.after(0, self.update_progress)
    
    def update_progress(self):
        if self.thread.is_alive():
            # 100 is the delay until tkinter does the next step
            self.master.after(100, self.update_progress)
        else:
            self.loading_label.config(text="Stuff Loaded!")