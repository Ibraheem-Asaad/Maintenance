
"""Maintenance Configurations"""

DEFAULT_ARG_FLAG = {
    'cclean': True,
    'clean': True,
    'dropbox': True,
    'onedrive': True,
    'update': True,
    'usb': True
}

CCLEANER_PATH = r'C:\Program Files\CCleaner'
DROPBOX_CLIENT_PATH = r'C:\Program Files (x86)\Dropbox\Client'
ONEDRIVE_PATH = r'C:\Users\brhoo_000\OneDrive\Backup'
DROPBOX_PATH = r'C:\Users\brhoo_000\Dropbox\Backup'
USB_PATH = r'I:\Backup'

BACKUP_PATHS = [
    r'E:\Notes',
    r'C:\Users\brhoo_000\Desktop',
    r'E:\Coding\Java\BumblebeeServer',
    r'E:\Coding\Python\Monitor',
    r'E:\Coding\Python\Bumblebee',
    r'E:\Coding\Utilities',
    r'E:\CV\Current CV'
]

# 10MB - in bytes
MAX_FILE_SIZE = 10 * 1024 * 1024
