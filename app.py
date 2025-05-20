from gui.main_window import DiskVisualizer
import platform

if __name__ == "__main__":
    if platform.system() != 'Windows':
        print("This app is only supported on Windows.")
    else:
        app = DiskVisualizer()
        app.mainloop()
