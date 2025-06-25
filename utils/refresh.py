from utils.drive_info import get_drive_info
from utils.logger import log_operation

def refresh_drive_info():
    try:
        drives = get_drive_info()
        log_operation("Refreshed drive information.")
        return drives
    except Exception as e:
        log_operation(f"Failed to refresh drive info: {e}")
        return []
