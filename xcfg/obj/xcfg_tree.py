#!/bin/python3
#coding:utf-8
from enum import Enum
from pprint import pformat

class xcfg_node():
    def __init__(self, name, father = None):
        self.__id = uuid
        self.__root = father.root if father is not None else self
        self.__father = father
        self.__index = {}
        self.__name = name
        self.__cellname = cellname


class xcfg_leaf(xcfg_node):
    def __init__(self, key, root = None):
        self.root = root
        self.xkey = xkey
        self.xval = xval

    def __str__(self):
        return f"{self.xkey} = {self.xval}"




# if __name__ == '__main__':
#     xobj = xcfg_object()
#     print(xobj.xpop(1))
#     print(xobj.xpop(1))
#     print(xobj.xput(1))
#     print(xobj.xput(1, 2))
#     print(xobj.xput(1, 2))
#     print(xobj.xset(1))
#     print(xobj.xset(5, 6))
#     print(xobj.xset(5, 7))
#     print(xobj)
#     print(xobj.xset(7, 8, 9))
#     print(xobj.set('7.9', 10))
#     print(xobj)
#     print(xobj.xput(7, 8, 9))
#     print(xobj.put('7.9', 10))
#     print(xobj)
#     print(xobj.set('7.9', 11))
#     print(xobj)
#     print(xobj.xput(10, 20, 30, 40, 50, 60, 70, 80, 90))
#     print(xobj.xput(10, 20, 30, 40, 50, 60, 70, 80))
#     print(xobj.xput(10, 20, 30, 40, 50, 60, 70))
#     print(xobj.xput(10, 20, 30, 40, 50, 60))
#     print(xobj.xput(10, 20, 30, 40, 50))
#     print(xobj)
#     print(xobj.xget(1))
#     print(xobj.xget(2))
#     print(xobj.xget(3))
#     print(xobj.xget(4))
#     print(xobj)
#     print(xobj.list())
#     for key in xobj.xlist():
#         print("{}:{}".format(key, xobj.xget(*key)))
#     print(xobj.show())
#     for key, value in xobj.xshow():
#         print("{}:{}".format(key, value))
#     print(xobj)
