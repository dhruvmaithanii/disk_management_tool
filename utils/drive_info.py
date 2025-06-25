import subprocess
import json

def get_drive_info():
    script = """
    $drives = Get-Volume | Where-Object { $_.DriveLetter -ne $null }
    $drives | ForEach-Object {
        $partition = Get-Partition -DriveLetter $_.DriveLetter
        $disk = Get-Disk -Number $partition.DiskNumber
        [PSCustomObject]@{
            DriveLetter      = $_.DriveLetter
            FileSystemLabel  = $_.FileSystemLabel
            Size             = $_.Size
            SizeRemaining    = $_.SizeRemaining
            PartitionNumber  = $partition.PartitionNumber
            DiskNumber       = $partition.DiskNumber
            Type             = $disk.PartitionStyle
            IsBoot           = $disk.IsBoot
            IsSystem         = $disk.IsSystem
            GptType          = $partition.GptType
        }
    } | ConvertTo-Json
    """

    result = subprocess.run(["powershell", "-Command", script],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception("PowerShell failed: " + result.stderr)

    return json.loads(result.stdout)
