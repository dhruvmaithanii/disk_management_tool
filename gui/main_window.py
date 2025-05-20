import tkinter as tk
from tkinter import ttk
from gui.widgets import create_drive_frame
from utils.drive_info import get_drive_info

class DiskVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Disk Partition Visualizer & Formatter")
        self.geometry("700x500")
        self.configure(bg="#eaeaea")

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure("TProgressbar", thickness=20, troughcolor='#d9d9d9', background="#4caf50")

        title = tk.Label(self, text="Disk Partition Visualizer & Formatter", font=("Segoe UI", 14, "bold"), bg="#eaeaea")
        title.pack(pady=10)

        self.frame_container = tk.Frame(self, bg="#eaeaea")
        self.frame_container.pack(fill="both", expand=True, padx=20)

        self.draw_ui()

    def draw_ui(self):
        drives = get_drive_info()

        for widget in self.frame_container.winfo_children():
            widget.destroy()

        for drive in drives:
            frame = create_drive_frame(self.frame_container, drive)
            frame.pack(padx=10, pady=10, fill="x")
