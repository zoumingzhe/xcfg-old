#!/bin/python3
#coding:utf-8

import sys
import argparse

from .config import xcfg_conf



def stdin_readlines():
    if not sys.stdin.isatty():
        stdin = sys.stdin.readlines()
        return ''.join(stdin)
    return None


class xcfg_parser():
    """
    """
    def __init__(self, prog):
        self.parser = argparse.ArgumentParser(prog = "xcfg-show")

    def parse_args(self):
        return self.parser.parse_args()

    def enable_type(self):
        self.parser.add_argument('-t', '--type', type=str, nargs='?',
                            choices=xcfg_conf.support_list,
                            help="specify configuration object type")

    def enable_debug(self):
        self.parser.add_argument('-d', '--debug', type=bool, nargs='?',
                                 default=False, const=True, help="debug")

    def enable_output(self):
        self.parser.add_argument('-o', '--output', type=str, nargs='?',
                            default=None, const='/tmp/xcfg-show',
                            help="specify output file or directory")

    def enable_object(self):
        stdin = stdin_readlines()
        self.parser.add_argument('object', type=str, nargs='?', default=stdin,
                                 help="specify configuration object")
