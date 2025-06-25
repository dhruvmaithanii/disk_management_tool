import subprocess
from utils.logger import log_operation

def format_volume(drive_letter, filesystem="NTFS", quick=True, label="NewVolume"):
    """
    Formats a volume with specified parameters.
    
    Args:
        drive_letter: The drive letter to format (without colon, e.g., 'D')
        filesystem: The filesystem to use (default: NTFS)
        quick: Whether to perform quick format (default: True)
        label: The volume label (default: 'NewVolume')
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Remove any trailing colon if provided
        drive_letter = drive_letter.rstrip(':').upper()
        
        # Build base command
        cmd_base = [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-Command",
            (
                f"Format-Volume -DriveLetter '{drive_letter}' "
                f"-FileSystem {filesystem} "
                f"-NewFileSystemLabel '{label}' "
                f"-Confirm:$false"
            )
        ]
        
        # Handle quick format attempt with fallback
        if quick:
            try:
                quick_cmd = cmd_base.copy()
                quick_cmd[-1] += " -Quick"
                result = subprocess.run(quick_cmd, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError:
                # Fall back to regular format if quick format fails
                result = subprocess.run(cmd_base, capture_output=True, text=True, check=True)
        else:
            result = subprocess.run(cmd_base, capture_output=True, text=True, check=True)
        
        log_operation(f"Formatted {drive_letter}: filesystem={filesystem}, quick={quick}, label={label}")
        return True, f"Drive {drive_letter}: formatted successfully as '{label}' using {filesystem}."

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr or e.stdout or "Unknown error occurred"
        log_operation(f"Failed to format {drive_letter}: {error_msg}")
        return False, f"Formatting failed: {error_msg}"
    except Exception as e:
        log_operation(f"Unexpected error formatting {drive_letter}: {str(e)}")
        return False, f"Unexpected error: {str(e)}"