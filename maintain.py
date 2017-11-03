
"""System Maintainance script - Clean, Backup, Update"""

from sys import argv as ARGV
from os import chdir, system
from update import fetch_key
from arg import parse_flags
from dirutil import copydir, cleandir
from configs import BACKUP_PATHS, CCLEANER_PATH, DEFAULT_ARG_FLAG, DROPBOX_PATH, \
    ONEDRIVE_PATH, USB_PATH


def main():
    """System Maintainance script - Clean, Backup, Update"""
    # If no flags were provided, use the default configurations
    global ARGV
    argv = ARGV
    if len(argv) == 1:
        arg_flag = DEFAULT_ARG_FLAG
    else:
        argv, arg_flag = parse_flags(
            argv, ['cclean', 'clean', 'dropbox', 'onedrive', 'update', 'usb'])

    backup_targets = []
    if arg_flag['onedrive']:
        backup_targets.append(ONEDRIVE_PATH)
    if arg_flag['dropbox']:
        raw_input("Start Dropbox, press Enter to continue...")
        backup_targets.append(DROPBOX_PATH)
    if arg_flag['usb']:
        raw_input("Insert a flash drive, press Enter to continue...")
        backup_targets.append(USB_PATH)

    for backup_target in backup_targets:
        chdir(backup_target)
        if arg_flag['clean']:
            cleandir(backup_target)
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
