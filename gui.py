import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from utils.format import format_volume
from utils.refresh import refresh_drive_info
from utils.shrink import shrink_volume
from utils.merge import merge_unallocated_space
from utils.protection import is_protected_drive

class DiskToolGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧩 Dynamic Disk Partition Tool")
        self.geometry("900x500")
        self.configure(bg="#1e1e2f")
        self.style = ttk.Style(self)
        self.set_theme()
        self.drive_data = []
        self.create_widgets()
        self.refresh_drives()

    def set_theme(self):
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                             background="#2e2e3e",
                             foreground="white",
                             rowheight=28,
                             fieldbackground="#2e2e3e",
                             bordercolor="#333")
        self.style.map("Treeview", background=[('selected', '#5e81ac')])
        self.style.configure("Treeview.Heading", background="#44475a", foreground="white", font=("Segoe UI", 10, "bold"))

        self.style.configure("TButton",
                             font=("Segoe UI", 10, "bold"),
                             background="#5e81ac",
                             foreground="white")
        self.style.map("TButton",
                       background=[('active', '#81a1c1')],
                       foreground=[('active', 'white')])

    def create_widgets(self):
        title_label = tk.Label(self, text="Dynamic Disk Partition Tool", bg="#1e1e2f",
                               fg="#88c0d0", font=("Segoe UI", 18, "bold"))
        title_label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("Letter", "Label", "Size", "Free"), show="headings")

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=130)

        self.tree.tag_configure("protected", background="#4c566a")
        self.tree.tag_configure("normal", background="#3b4252")

        self.tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        btn_frame = tk.Frame(self, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="🔽 Shrink", command=self.handle_shrink).pack(side=tk.LEFT, padx=12)
        ttk.Button(btn_frame, text="🧩 Merge", command=self.handle_merge).pack(side=tk.LEFT, padx=12)
        ttk.Button(btn_frame, text="🔄 Refresh", command=self.refresh_drives).pack(side=tk.LEFT, padx=12)
        ttk.Button(btn_frame, text="🔄 Format", command=self.handle_format).pack(side=tk.LEFT, padx=12)

    def refresh_drives(self):
        self.tree.delete(*self.tree.get_children())
        self.drive_data = refresh_drive_info()

        for drive in self.drive_data:
            if drive["DriveLetter"]:
                size_gb = int(drive["Size"]) // (1024**3)
                free_gb = int(drive["SizeRemaining"]) // (1024**3)
                tag = "protected" if is_protected_drive(drive["DriveLetter"]) else "normal"
                self.tree.insert("", tk.END, values=(
                    drive["DriveLetter"],
                    drive["FileSystemLabel"],
                    f"{size_gb} GB",
                    f"{free_gb} GB",
                    ), tags=(tag,))


    def get_selected_drive(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a drive first.")
            return None
        values = self.tree.item(selected)["values"]
        return values[0]  # Drive letter

    def handle_shrink(self):
        drive = self.get_selected_drive()
        if not drive:
            return
        if is_protected_drive(drive):
            messagebox.showerror("Protected", f"Drive {drive} is protected and cannot be modified.")
            return
        try:
            shrink_mb = simpledialog.askinteger("Shrink Volume", "Enter size to shrink (in MB):", minvalue=1)
            if shrink_mb:
                success, msg = shrink_volume(drive, shrink_mb)
                messagebox.showinfo("Shrink Result", msg)
                if success:
                    self.refresh_drives()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_merge(self):
        drive = self.get_selected_drive()
        if not drive:
            return
        if is_protected_drive(drive):
            messagebox.showerror("Protected", f"Drive {drive} is protected and cannot be modified.")
            return
        success, msg = merge_unallocated_space(drive)
        messagebox.showinfo("Merge Result", msg)
        if success:
            self.refresh_drives()
            
    def handle_format(self):
        drive = self.get_selected_drive()
        if not drive:
            return
        if is_protected_drive(drive):
            messagebox.showerror("Protected", f"Drive {drive} is protected and cannot be formatted.")
            return
        confirm = messagebox.askyesno("Confirm Format", f"Are you sure you want to format drive {drive}? All data will be lost.")
        if not confirm:
            return
        filesystem = "NTFS"
        label = "FormattedDrive"

        success, msg = format_volume(drive, filesystem=filesystem, quick=True, label=label)
        messagebox.showinfo("Format Result", msg)

        if success:
            self.refresh_drives()


if __name__ == "__main__":
    app = DiskToolGUI()
    app.mainloop()
