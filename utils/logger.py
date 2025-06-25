import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), '..', 'disk_operations.log')

def log_operation(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
