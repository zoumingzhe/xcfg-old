#!/bin/python3
#coding:utf-8
from enum import Enum
from pprint import pformat


# TODO: key and value is not string
# TODO: tree node leaf

class xcfg_object():
    """
    """
    def __init__(self, name, prog = None):
        self.__id = uuid
        self.__store = {}
        self.__root = xcfg_node(name)

    def __str__(self):
        lines = []
        for key, value in self.show():
            lines.append("{} = {}".format(key, value))
        return '\n'.join(lines)

    def __each(self, store, prefix = []):
        keys = []
        for key in store:
            value = store.get(key)
            if type(value) is dict:
                keys.extend(self.__each(value, prefix + [key]))
            else:
                keys.append(tuple(prefix + [key]))
        return keys

    def xlist(self):
        keys = []
        store = self.__store
        for key in store:
            value = store.get(key)
            if type(value) is dict:
                keys.extend(self.__each(value, [key]))
            else:
                keys.append(tuple([key]))
        return keys

    def list(self):
        keys = []
        for key in self.xlist():
            keys.append('.'.join(key))
        return keys

    def xshow(self):
        values = []
        for key in self.xlist():
            value = self.xget(*key)
            values.append((key, value))
        return values

    def show(self):
        values = []
        for key, value in xobj.xshow():
            human = '.'.join(key)
            values.append((human, value))
        return values

    def xpop(self, *args, **kwargs):
        if len(args) < 1:
            return None
        store = self.__store
        for key in args[:-1]:
            store = store.get(key)
            if store is None:
                return None
        return store.pop(args[-1], None)

    def pop(self, human, **kwargs):
        return self.pop(*human.split('.'), **kwargs)

    def xget(self, *args, **kwargs):
        store = self.__store
        for key in args:
            store = store.get(key)
            if store is None:
                break
        return store

    def get(self, human, **kwargs):
        return self.xget(*human.split('.'), **kwargs)

    def xset(self, *args, **kwargs):
        if len(args) < 2:
            return False
        keys = [str(k) for k in args[:-1]]
        store = self.__store
        for key in keys[:-1]:
            if key not in store:
                return False
            store = store[key]
        if keys[-1] not in store:
            return False
        store[keys[-1]] = args[-1]
        return True

    def set(self, human, value, **kwargs):
        return self.xset(*human.split('.'), value, **kwargs)

    def xput(self, *args, **kwargs):
        if len(args) < 2:
            return False
        keys = [str(k) for k in args[:-1]]
        store = self.__store
        for key in keys[:-1]:
            store = store.setdefault(key, {})
            if type(store) is not dict:
                return False
        if keys[-1] in store:
            return False
        store[keys[-1]] = args[-1]
        return True

    def put(self, human, value, **kwargs):
        return self.xput(*human.split('.'), value, **kwargs)



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
