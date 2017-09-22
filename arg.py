
"""Utility function for parsing flags from arguments"""


def parse_flags(args, flags_list):
    """Parse arguments and return True/False for each flag argument"""
    flags = {}
    for flag in flags_list:
        flag_string = '-' + flag
        if flag_string in args:
            flags[flag] = True
            args.remove(flag_string)
        else:
            flags[flag] = False
    return args, flags
