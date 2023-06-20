from app.GUI.frame_manager import FrameManager
from app.Utils.app_settings_data import AppSettings


if __name__ == "__main__":
    settings = AppSettings(app_name="Simple Mono-SLAM", version="0.1", debug_mode=True, theme="Light", language="English")
    app = FrameManager()
    app.mainloop()