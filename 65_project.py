import win32api

available_drives = win32api.GetLogicalDriveStrings()
print(available_drives)

drives = [drivestr for drivestr in available_drives.split('\000') if drivestr]
drives=drives
print(drives)