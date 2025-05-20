import tkinter as tk
from tkinter import ttk, messagebox
from utils.formatter import format_drive
from utils.constants import PROTECTED_DRIVES

def create_drive_frame(parent, drive):
    frame = tk.Frame(parent, bg="#ffffff", bd=1, relief=tk.RIDGE)

    label = tk.Label(frame, text=f"{drive['label']}\n{drive['used']} GB used / {drive['total']} GB", 
                     font=("Segoe UI", 10), bg="#ffffff")
    label.pack(anchor="w", padx=10, pady=2)

    progress = ttk.Progressbar(frame, length=500, value=drive['percent'])
    progress.pack(padx=10, pady=5)

    if drive['volume_label'] not in PROTECTED_DRIVES and drive['device'].strip(':\\') not in PROTECTED_DRIVES:
        btn = tk.Button(frame, text="Format", bg="#ff4d4d", fg="white", 
                        command=lambda m=drive['mountpoint']: format_drive(m))
        btn.pack(padx=10, pady=5, anchor="e")
    else:
        tk.Label(frame, text="Protected Drive", fg="gray", bg="#ffffff").pack(padx=10, pady=5, anchor="e")

    return frame
