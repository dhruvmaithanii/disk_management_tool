import psutil
import wmi

def get_drive_info():
    drives = []
    c = wmi.WMI()

    for disk_index, disk in enumerate(c.Win32_DiskDrive()):
        for partition in disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                try:
                    mountpoint = logical_disk.DeviceID
                    usage = psutil.disk_usage(mountpoint)
                    total_gb = round(usage.total / (1024**3), 2)
                    free_gb = round(usage.free / (1024**3), 2)
                    used_gb = round(usage.used / (1024**3), 2)
                    percent_used = usage.percent

                    volume_label = logical_disk.VolumeName or "Unknown"

                    label = f"Disk {disk_index + 1} - {volume_label} ({mountpoint})"

                    drives.append({
                        'device': mountpoint,
                        'mountpoint': mountpoint,
                        'fstype': logical_disk.FileSystem or "",
                        'label': label,
                        'volume_label': volume_label,
                        'total': total_gb,
                        'free': free_gb,
                        'used': used_gb,
                        'percent': percent_used
                    })
                except Exception:
                    continue
    return drives
