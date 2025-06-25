def is_protected_drive(drive_letter):
    """
    Checks if the drive is protected. Returns True if protected.
    """
    return drive_letter.upper() == "C"
