from tkinter import simpledialog, messagebox
import subprocess

def shrink_volume(mountpoint):
    letter = mountpoint.strip(':\\')
    try:
        shrink_mb = simpledialog.askinteger("Shrink Volume", f"Enter amount to shrink {letter}: in MB")
        if not shrink_mb or shrink_mb <= 0:
            return

        powershell_cmd = f"powershell -Command \"Get-Partition -DriveLetter {letter} | Resize-Partition -Size ((Get-Partition -DriveLetter {letter}).Size - {shrink_mb}MB)\""

        confirm = messagebox.askyesno("Confirm Shrink", f"Shrink {letter}: by {shrink_mb} MB?")
        if confirm:
            subprocess.run(powershell_cmd, shell=True, check=True)
            messagebox.showinfo("Success", f"{letter}: drive shrunk by {shrink_mb} MB.")

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to shrink volume: {str(e)}")
