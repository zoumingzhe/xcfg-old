#!/bin/python3
# coding:utf-8

import os
import sys
import errno

from .xcfg_show import main as xcfg_show

sub_command = {
    "list": (None, "List all stored configurations"),
    "show": (xcfg_show, "Show the specified configuration"),
    "help": (None, "Show command's help message"),
}


def usage():
    name = os.path.basename(sys.argv[0])
    print("Usage: {} <command> [<args>]\n".format(name))
    print("{}\n".format("Once configured, Use anywhere."))
    print("Command list:")
    for cmd in sub_command:
        print("    {}\t{}".format(cmd, sub_command[cmd][1]))


def help():
    cmd = sys.argv[2] if len(sys.argv) > 2 else None

    if cmd not in sub_command:
        usage()
        exit(errno.ENOENT)

    sys.argv = [sys.argv[0], cmd, '--help']
    sub_command[cmd][0]()


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in sub_command:
        usage()
        exit(errno.ENOENT)

    cmd = sys.argv[1]
    if cmd == "help":
        help()
    else:
        sys.argv.pop(1)
        sub_command[cmd][0]()


if __name__ == '__main__':
    main()
