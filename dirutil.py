
"""Directory utility functions for maintenance script"""

from time import strftime
from os import listdir, mkdir, path
from fnmatch import fnmatch
from shutil import copy2
from configs import MAX_FILE_SIZE


def generate_name(path):
    """Generate folder name based on it's path and creation date"""
    # TODO: change date to y-m-d
    return '(' + strftime('%x').replace('/', '.') + ') ' + path.replace(':', '').replace('\\', '.')


# def generate_name_pattern(path):
#     """Generate folder patter for deleting old backups"""
#     return path.replace(':', '').replace('\\', '.') + ' (*)'

# TODO: use the new pattern to delete old backups
def generate_name_pattern():
    """Generate folder patter for deleting old backups"""
    return '(*.*.*) *'


def copydir(src, dest):
    """Copy a directory with it's contents that conform to certain criterias"""
    folder_name = path.basename(src)
    new_folder = path.join(dest, folder_name)
    mkdir(new_folder)
    dest = new_folder
    for name in listdir(src):
        # TODO: make sure it's not hidden
        if not fnmatch(name, '~*') and not fnmatch(name, '.*'):
            src_path = path.join(src, name)
            if path.isdir(src_path):
                copydir(src_path, dest)
            else:
                dest_path = path.join(dest, name)
                # Make only a shell for big files
                if path.getsize(src_path) > MAX_FILE_SIZE:
                    print 'Copying ' + src_path + ' as shell'
                    with open(str(dest_path), 'w') as shell:
                        pass
                else:
                    copy2(src_path, dest_path)
