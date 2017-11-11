
"""Utility function for parsing flags from arguments"""
from configs import DEFAULT_ARG_FLAG


def parse_flags(args, flags_set):
    """Parse arguments and return True/False for each flag argument"""
    # If no flags were provided, use the default configurations
    if len(args) == 1:
        return args, DEFAULT_ARG_FLAG
    flags = {}
    for flag in flags_set:
        flag_string = '-' + flag
        if flag_string in args:
            flags[flag] = True
            args.remove(flag_string)
        else:
            flags[flag] = False
    return args, flags
