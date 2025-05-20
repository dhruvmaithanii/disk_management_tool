import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from utils.drive_info import get_drive_info
from utils.formatting import format_drive
from utils.shrink import shrink_volume
from gui.widgets import create_partition_frame

PROTECTED_DRIVES = ['C', 'System Reserved', 'Recovery', 'EFI']

class DiskVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Disk Partition Visualizer & Formatter")
        self.geometry("800x600")
        self.configure(bg="#eaeaea")

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure("TProgressbar", thickness=20, troughcolor='#d9d9d9', background="#4caf50")

        title = tk.Label(self, text="Disk Partition Visualizer & Formatter", font=("Segoe UI", 14, "bold"), bg="#eaeaea")
        title.pack(pady=10)

        canvas = tk.Canvas(self, bg="#eaeaea")
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.frame_container = tk.Frame(canvas, bg="#eaeaea")

        self.frame_container.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.frame_container, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.draw_ui()

    def draw_ui(self):
        drives = get_drive_info()

        for widget in self.frame_container.winfo_children():
            widget.destroy()

        for i, drive in enumerate(drives):
            frame = create_partition_frame(self.frame_container, drive)

            button_frame = tk.Frame(frame, bg="#ffffff")
            button_frame.pack(anchor="e", padx=10, pady=5)

            if drive['volume_label'] not in PROTECTED_DRIVES and drive['device'].strip(':\\') not in PROTECTED_DRIVES:
                tk.Button(button_frame, text="Format", bg="#ff4d4d", fg="white", 
                          command=lambda m=drive['mountpoint']: format_drive(m)).pack(side="left", padx=5)
                tk.Button(button_frame, text="Shrink", bg="#4d79ff", fg="white", 
                          command=lambda m=drive['mountpoint']: shrink_volume(m)).pack(side="left", padx=5)
            else:
                tk.Label(button_frame, text="Protected Drive", fg="gray", bg="#ffffff").pack()
