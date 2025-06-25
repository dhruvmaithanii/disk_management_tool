import subprocess
from utils.logger import log_operation

def shrink_volume(drive_letter, shrink_mb):
    try:
        script = f"""
        $vol = Get-Volume -DriveLetter {drive_letter}
        $part = Get-Partition -DriveLetter {drive_letter}
        $sizeToShrink = {shrink_mb}MB
        Resize-Partition -DriveLetter {drive_letter} -Size ($part.Size - $sizeToShrink)
        """
        result = subprocess.run(["powershell", "-Command", script],
                                capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception(result.stderr)

        log_operation(f"Shrunk {drive_letter}: by {shrink_mb}MB.")
        return True, f"Successfully shrunk drive {drive_letter} by {shrink_mb}MB."

    except Exception as e:
        log_operation(f"Failed to shrink {drive_letter}: {e}")
        return False, str(e)
