
"""Directory utility functions for maintenance script"""

from glob import glob
from os import listdir, mkdir, path, rename
from fnmatch import fnmatch
from shutil import copy2, rmtree
from configs import MAX_FILE_SIZE


def generate_name(path):
    """Generate folder name based on it's path"""
    return path.replace(':', '').replace('\\', '.').replace(' ', '_')


def generate_old_name(name):
    """Generate new name for old folders"""
    return '_' + name


def generate_old_name_pattern():
    """Generate folder patter for deleting old backups"""
    return '_*'


def cleandir(dest):
    """Rename old backups and delete older ones"""
    old_backups = glob(generate_old_name_pattern())
    for old_backup in old_backups:
        rmtree(old_backup)
    for name in listdir(dest):
        rename(name, generate_old_name(name))


def copydir(src, dest):
    """Copy a directory with a name corresponding to it's path"""
    copydir_aux(src, dest, generate_name(src))


def copydir_aux(src, dest, new_folder):
    """Copy a directory with it's contents that conform to certain criterias"""
    if new_folder is None:
        new_folder = path.join(dest, path.basename(src))
    mkdir(new_folder)
    dest = new_folder
    for name in listdir(src):
        if not fnmatch(name, '~*') and not fnmatch(name, '.*'):
            src_path = path.join(src, name)
            if path.isdir(src_path):
                copydir(src_path, dest)
            else:
                dest_path = path.join(dest, name)
                # Make only a shell for big files
                if path.getsize(src_path) > MAX_FILE_SIZE:
                    print 'Copying ' + src_path + ' only as shell!'
                    with open(str(dest_path), 'w') as shell:
                        pass
                else:
                    copy2(src_path, dest_path)
