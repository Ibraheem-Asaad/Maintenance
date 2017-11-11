
"""Maintenance Configurations"""

DEFAULT_ARG_FLAG = {
    'cclean': True,
    'clean': False,
    'dropbox': True,
    'onedrive': True,
    'update': True,
    'usb': True
}

CCLEANER_PATH = r'C:\Program Files\CCleaner'
ONEDRIVE_PATH = r'C:\Users\brhoo_000\OneDrive\Backup'
DROPBOX_PATH = r'C:\Users\brhoo_000\Dropbox\Backup'
USB_PATH = r'I:\Backup'

BACKUP_PATHS = [
    r'E:\Notes',
    r'E:\CV\Current CV'
]

# 10MB - in bytes
MAX_FILE_SIZE = 10 * 1024 * 1024
