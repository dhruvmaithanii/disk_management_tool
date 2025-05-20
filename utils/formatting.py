import subprocess
from tkinter import messagebox

PROTECTED_DRIVES = ['C', 'System Reserved', 'Recovery', 'EFI']

def format_drive(mountpoint):
    try:
        drive_letter = mountpoint.strip(':\\')
        if drive_letter.upper() in PROTECTED_DRIVES:
            messagebox.showwarning("Protected Drive", "This drive is protected and cannot be formatted.")
            return

        confirm = messagebox.askyesno("Confirm Format", f"Are you sure you want to format {mountpoint}? This will erase all data.")
        if not confirm:
            return

        cmd = f'format {mountpoint} /FS:NTFS /Q /Y'
        subprocess.run(cmd, shell=True, check=True)
        messagebox.showinfo("Success", f"{mountpoint} formatted successfully.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to format the drive.")
