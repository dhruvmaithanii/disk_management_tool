# 💽 Dynamic Disk Tool – Windows Partition Manager with Python GUI

> A complete utility to manage, format, shrink, and refresh drives on Windows — built in Python with a clean Tkinter GUI and modular backend.

---

## 📌 Project Overview

Dynamic Disk Tool is a Python-based GUI utility for disk partition management. It interacts with the Windows disk subsystem using system commands and scripts while offering a user-friendly interface. From drive info to formatting and shrinking partitions, this tool covers essential disk operations with logging and safety in mind.

---

## ✅ Features

- 🔍 View current drive information
- ✂️ Shrink volumes dynamically
- 🧩 Merge or refresh disk volumes
- 🔐 Enable/disable write protection
- 🧼 Format partitions safely
- 🪟 GUI interface with Tkinter
- 📝 Logs every operation for traceability

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Tkinter** – GUI interface
- **Windows CMD/Diskpart** – Backend execution
- **Logging** – Activity tracking
- **Modular utilities** – Clean separation of features

---

## 🗂️ Project Structure

```
dynamic_disk_tool/
│
├── main.py                # Entry point to launch the tool
├── gui.py                 # Tkinter GUI logic
├── disk_operations.log    # Logs user actions and operations
├── utils/
│   ├── drive_info.py      # Detects connected drives
│   ├── shrink.py          # Handles shrinking of volumes
│   ├── format.py          # Formats partitions
│   ├── merge.py           # Logic for merging disk partitions
│   ├── refresh.py         # Refreshes disk status
│   ├── protection.py      # Enables/disables write protection
│   ├── logger.py          # Centralized logging system
│   └── __init__.py
```

---

## 💻 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/dynamic_disk_tool.git
cd dynamic_disk_tool
```

### 2. (Optional) Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/Scripts/activate   # On Windows
pip install -r requirements.txt
```

### 3. Run the App

```bash
python main.py
```

> ⚠️ **Run with Administrator Privileges** for disk operations to execute correctly.

---

## 📋 Requirements

- **Windows OS**
- Python 3.10+
- Admin privileges for disk-level commands
- `tkinter` (comes with Python)

---

## 🧪 Demo

![screenshot or gif placeholder]

---

## 👥 Team Contributions

- **Dhruv Maithani** 
- **Pranav Chamoli**
- **Animesh Mamgain**
- **Priyanshu Bisht**

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome. For suggestions, improvements, or bug fixes, feel free to fork and submit a PR.

---

## 🙋‍♂️ Support

Have questions or want to report an issue? Open an issue on GitHub or reach out via LinkedIn.

---

