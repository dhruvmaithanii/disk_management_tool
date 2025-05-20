import tkinter as tk
from tkinter import ttk

def create_partition_frame(parent, drive):
    # Create partition frame with a progress bar
    frame = tk.Frame(parent, bg="#ffffff", bd=1, relief=tk.RIDGE)
    frame.pack(padx=10, pady=10, fill="x")

    label = tk.Label(frame, text=f"{drive['label']}\n{drive['used']} GB used / {drive['total']} GB", 
                     font=("Segoe UI", 10), bg="#ffffff")
    label.pack(anchor="w", padx=10, pady=2)

    progress = ttk.Progressbar(frame, length=500, value=drive['percent'])
    progress.pack(padx=10, pady=5)

    return frame
