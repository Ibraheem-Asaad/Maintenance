
"""System Maintainance script - Clean, Backup, Update"""

from sys import argv as ARGV
from os import chdir, path, rename, system
from shutil import rmtree
from glob import glob
from update import fetch_key
from arg import parse_flags
from dirutil import copydir, generate_name_pattern, generate_name
from configs import BACKUP_PATHS, CCLEANER_PATH, DEFAULT_ARG_FLAG, DROPBOX_PATH, \
    ONEDRIVE_PATH, USB_PATH

# If no flags were provided, use the default configurations
if len(ARGV) == 1:
    ARG_FLAG = DEFAULT_ARG_FLAG
else:
    ARGV, ARG_FLAG = parse_flags(
        ARGV, ['cclean', 'clean', 'dropbox', 'onedrive', 'update', 'usb'])

BACKUP_TARGETS = []
if ARG_FLAG['onedrive']:
    BACKUP_TARGETS.append(ONEDRIVE_PATH)
if ARG_FLAG['dropbox']:
    raw_input("Start Dropbox, press Enter to continue...")
    BACKUP_TARGETS.append(DROPBOX_PATH)
if ARG_FLAG['usb']:
    raw_input("Insert a flash drive, press Enter to continue...")
    BACKUP_TARGETS.append(USB_PATH)

# TODO: change to overwrite changed files
for backup_target in BACKUP_TARGETS:
    chdir(backup_target)
    for backup_path in BACKUP_PATHS:
        copydir(backup_path, backup_target)
        if ARG_FLAG['clean']:
            OLD_BACKUPS = glob(generate_name_pattern(backup_path))
            if len(OLD_BACKUPS) > 0:
                print 'Found older backups in ' + backup_target + ':-'
                print OLD_BACKUPS
                if raw_input("Delete? (y/n) :>") == 'y':
                    for old_backup in OLD_BACKUPS:
                        rmtree(old_backup)
        rename(path.basename(backup_path), generate_name(backup_path))

if ARG_FLAG['update']:
    fetch_key()

if ARG_FLAG['cclean']:
    raw_input("Close any open browsers, press Enter to continue...")
    chdir(CCLEANER_PATH)
    system('CCleaner64 /auto')
    print 'Ccleaner is running in the background...'
    raw_input("Clean registery and restart!")

print 'Maintainance was completed successfully'
