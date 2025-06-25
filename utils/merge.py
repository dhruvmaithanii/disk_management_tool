import subprocess
from utils.logger import log_operation

def merge_unallocated_space(drive_letter):
    try:
        script = f"""
        $partition = Get-Partition -DriveLetter {drive_letter}
        $disk = Get-Disk -Number $partition.DiskNumber
        $sizeBefore = $partition.Size
        Resize-Partition -DriveLetter {drive_letter} -Size ($disk | Get-PartitionSupportedSize -PartitionNumber $partition.PartitionNumber).SizeMax
        """
        result = subprocess.run(["powershell", "-Command", script],
                                capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception(result.stderr.strip())

        log_operation(f"Merged unallocated space into drive {drive_letter}.")
        return True, f"Successfully merged unallocated space into {drive_letter}."

    except Exception as e:
        log_operation(f"Failed to merge unallocated space into {drive_letter}: {e}")
        return False, str(e)
