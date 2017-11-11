
"""System Maintainance script - Clean, Backup, Update"""

from sys import argv as ARGV
from os import chdir, system
from update import fetch_key
from arg import parse_flags
from dirutil import copydir, cleandir, renamedir
from configs import BACKUP_PATHS, CCLEANER_PATH, DROPBOX_PATH, ONEDRIVE_PATH, USB_PATH


def main():
    """System Maintainance script - Clean, Backup, Update"""

    argv, arg_flag = parse_flags(
        ARGV, {'cclean', 'clean', 'dropbox', 'onedrive', 'update', 'usb'})

    backup_targets = set()
    if arg_flag['onedrive']:
        backup_targets.add(ONEDRIVE_PATH)
    if arg_flag['dropbox']:
        raw_input("Start Dropbox, press Enter to continue...")
        backup_targets.add(DROPBOX_PATH)
    if arg_flag['usb']:
        raw_input("Insert a flash drive, press Enter to continue...")
        backup_targets.add(USB_PATH)

    for backup_target in backup_targets:
        chdir(backup_target)
        if arg_flag['clean']:
            cleandir(backup_target)
        renamedir(backup_target)
        for backup_path in BACKUP_PATHS:
            copydir(backup_path, backup_target)

    if arg_flag['update']:
        fetch_key()

    if arg_flag['cclean']:
        raw_input("Close any open browsers, press Enter to continue...")
        chdir(CCLEANER_PATH)
        system('CCleaner64 /auto')
        print 'Ccleaner is running in the background...'
        raw_input("Clean registery and restart!")

    print 'Maintainance was completed successfully'


if __name__ == '__main__':
    main()
