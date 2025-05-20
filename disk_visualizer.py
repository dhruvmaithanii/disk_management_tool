import tkinter as tk
from tkinter import ttk
import psutil
import wmi

# === Helper Function ===
def get_drive_info():
    drives = []
    c = wmi.WMI()

    for disk_index, disk in enumerate(c.Win32_DiskDrive()):
        for partition in disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                try:
                    mountpoint = logical_disk.DeviceID
                    usage = psutil.disk_usage(mountpoint)
                    total_gb = round(usage.total / (1024**3), 2)
                    free_gb = round(usage.free / (1024**3), 2)
                    used_gb = round(usage.used / (1024**3), 2)
                    percent_used = usage.percent

                    volume_label = logical_disk.VolumeName or "Unknown"

                    # Label based on disk and partition
                    label = f"Disk {disk_index + 1} - {volume_label} ({mountpoint})"

                    drives.append({
                        'device': mountpoint,
                        'mountpoint': mountpoint,
                        'fstype': logical_disk.FileSystem or "",
                        'label': label,
                        'volume_label': volume_label,
                        'total': total_gb,
                        'free': free_gb,
                        'used': used_gb,
                        'percent': percent_used
                    })
                except Exception:
                    continue

    return drives


# === GUI Setup ===
class DiskVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Disk Partition Visualizer")
        self.geometry("800x600")
        self.configure(bg="#eaeaea")

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure("TProgressbar", thickness=20, troughcolor='#d9d9d9', background="#4caf50")

        title = tk.Label(self, text="Disk Partition Visualizer", font=("Segoe UI", 14, "bold"), bg="#eaeaea")
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
            frame = tk.Frame(self.frame_container, bg="#ffffff", bd=1, relief=tk.RIDGE)
            frame.pack(padx=10, pady=10, fill="x")

            label = tk.Label(frame, text=f"{drive['label']}\n{drive['used']} GB used / {drive['total']} GB", 
                             font=("Segoe UI", 10), bg="#ffffff")
            label.pack(anchor="w", padx=10, pady=2)

            progress = ttk.Progressbar(frame, length=500, value=drive['percent'])
            progress.pack(padx=10, pady=5)


if __name__ == "__main__":
    app = DiskVisualizer()
    app.mainloop()
