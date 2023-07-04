import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
from threading import Thread
from ..Utils.app_settings_data import AppSettings
import time, os
import numpy as np
from typing import List

# Delete all calibration images
# restart calibration
# start calibration
# delete calibration data button

class CameraCalib(tk.Frame):


    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text="Camera Calibration", font=("Arial", 18))
        label.pack(pady=20)
        
        button_start = tk.Button(self, text="Start capturing calibration images", command=self.start_video)
        button_start.pack()
        
        button_stop = tk.Button(self, text="Stop capturing calibration images", command=self.stop_video)
        button_stop.pack()
        
        button_calibrate = tk.Button(self, text="Calibrate Camera", command=self.calibrate_camera)
        button_calibrate.pack()

        button_back = tk.Button(self, text="Back to Menu", command=self.__del__)
        button_back.pack()
        
        # Video label
        self.video_label = ttk.Label(self)
        self.video_label.pack()

        # get settings
        self.app_settings = AppSettings.get_instance()
        
        # Get the default frame size
        self.cap = cv2.VideoCapture(self.app_settings.get_current_cam_index())
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.cap.release()

        # Thread variables
        self.thread = None
        self.is_running = False
        
        #cam calib variables -> TODO: Move Constants to data class 
        self.capture_countdown=5
        self.capture_count=0
        self.capture_count_max= 25
        self.is_capturing = True
        self.max_frame_time = 150
        
        self.cam_calib_img_path = self.app_settings.get_calib_img_path()
        self.calib_params_path = self.app_settings.get_calib_params_path()


    def start_video(self):
        print("start video")
        if not self.is_running:
            self.cap = cv2.VideoCapture(self.app_settings.get_current_cam_index())
            self.is_running = True
            self.thread = Thread(target=self.update_frame)
            self.thread.start()


    def update_frame(self):
        while self.is_running:
            ret, frame = self.cap.read()
            if ret:
                # Convert  BGR to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Resize the frame to fit within the Tkinter frame
                frame_resized = cv2.resize(frame_rgb, (self.width, self.height))
                if self.is_capturing:
                    frame_with_chessboard = self.find_chessboard(frame_resized)
                else: 
                    frame_with_chessboard = frame_resized
                # Convert the frame to PIL Image format
                image = Image.fromarray(frame_with_chessboard)

                # Create Tkinter-compatible photo image
                photo = ImageTk.PhotoImage(image)

                # Update the Tkinter label with the new frame
                self.video_label.configure(image=photo)
                self.video_label.image = photo


    def stop_video(self):
        if self.is_running:
            # Stop the video capture thread
            self.is_running = False
            self.cap.release()
            cv2.destroyAllWindows()
            
            if self.thread and self.thread.is_alive():
                self.thread.join(timeout=1)


    def __del__(self):
        self.stop_video()
        # self.cap.release()
        # cv2.destroyAllWindows()
        self.video_label.image = None
        self.master.show_frame(self.master.main_frame)
        

    def find_chessboard(self, frame):
        found, corners = cv2.findChessboardCorners(frame, (9, 6), None)
        
        if found:
            tmp_frame = frame.copy()
            cv2.drawChessboardCorners(frame, (9, 6), corners, found)
            
            if self.capture_countdown == 0:
                
                self.save_frame(tmp_frame)
                
                self.capture_count += 1
                
                if self.capture_count == self.capture_count_max:
                    self.show_capture_complete_message()
                    self.is_capturing = False
                self.capture_countdown = self.max_frame_time
            else: 
                self.capture_countdown -=1
        else:
            self.capture_countdown = self.max_frame_time
        
        countdown_text = f"Capture Countdown: {self.capture_countdown}"
        cv2.putText(frame, countdown_text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        return frame


    # TODO -> Optimize -> Car for calib_img_path
    def save_frame(self, frame):
        if not os.path.exists(self.cam_calib_img_path):
            os.makedirs(self.cam_calib_img_path)
        
        timestamp = int(time.time())
        filename = f"{self.cam_calib_img_path}/image_{timestamp}.jpg"
        
        cv2.imwrite(filename, frame)
        
        print(f"Saved image: {filename}")


    def show_capture_complete_message(self):
        messagebox.showinfo("Capture Complete", "Image capture complete. You can start calibration now")

        
    def calibrate_camera(self):
        print("calibrate camera")
        # 3d pts
        obj_pts = []
        # 2d image pts
        img_pts = []
        # chessboard
        chessboard_size = (9,6)
        
        objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
        
        images = self.load_calibration_images()
        print(images)
        for image in images:
            print(image)
            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)
            
            if ret: 
                obj_pts.append(objp)
                img_pts.append(corners)
            else:
                print("no corners")
        
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_pts, img_pts, gray.shape[::-1], None, None)

        print(mtx)
        print(dist)
        self.save_calibration_results(mtx, dist)
        return mtx, dist
            
    
    def load_calibration_images(self) -> List[str]:
        print("Loading Calibration images from disk")
        image_List = []
        for image in os.listdir(self.cam_calib_img_path):
            tmp_path =os.path.join(self.cam_calib_img_path, image)
            if os.path.isfile(tmp_path):
                image_List.append(tmp_path)
        # count images of not like max then prompt error
        if not image_List.__len__() == self.capture_count_max:
            messagebox.showinfo("Not enough images", f"For calibration you need {self.capture_count_max} images in {self.cam_calib_img_path}")
        return image_List
    
    def save_calibration_results(self, mtx, dist):
        
        if not os.path.exists(self.calib_params_path):
            os.makedirs(self.calib_params_path)
        
        filename = f"{self.calib_params_path}/cam_calib.yaml"
        
        fs = cv2.FileStorage(filename, cv2.FILE_STORAGE_WRITE)
        fs.write("camera_matrix", mtx)
        fs.write("distortion_coefficients", dist)
        fs.release()
        