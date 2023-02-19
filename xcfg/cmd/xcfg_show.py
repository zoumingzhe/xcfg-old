#!/bin/python3
# coding:utf-8

import sys
# import argparse

from ..utils.parser import xcfg_parser


def main():
    parser = xcfg_parser('xcfg-show')
    parser.enable_type()
    parser.enable_debug()
    parser.enable_output()
    parser.enable_object()
    xcfg_args = parser.parse_args()
    print(xcfg_args)


if __name__ == '__main__':
    main()
