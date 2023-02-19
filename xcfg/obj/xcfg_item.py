#!/bin/python3
# coding:utf-8
import re
from enum import Enum
from enum import unique

# TODO: key and value is not string
# TODO: tree node leaf

# class xcfg_type():
#     bool    = "bool"
#     datetime= "datetime"


@unique
class xcfg_type(Enum):
    bool = 1
    string = 2
    number = 3
    float = 4
    array = 5
    check = 6  # not guess 不猜测
    choice = 7  # not guess 不猜测
    datetime = 20
    date = 21
    time = 22
    timezone = 23


class xcfg_name():
    SEPARATOR = '.'
    CHARACTER = u'^[\-_a-zA-Z0-9]+$'

    @classmethod
    def join(cls, *args):
        for cell in args:
            assert type(cell) is str
        name = cls.SEPARATOR.join(args)
        return cls(name)

    def __init__(self, name):
        assert type(name) is str and name != ''
        self.__human = name
        self.__cells = tuple(name.split('.'))
        for cell in self.__cells:
            assert re.search(self.CHARACTER, cell)

    def __repr__(self):
        return self.__human

    def __str__(self):
        return self.__human

    def __get_cells(self):
        return self.__cells

    def __get_human(self):
        return self.__human

    cells = property(__get_cells)
    human = property(__get_human)


# xcfg_value
class xcfg_attr():

    def __init__(self, xtype, default=None, description=None):
        # assert type(name) is str and name != ''
        self.__xtype = xtype
        self.__default = default
        self.__description = description

    @staticmethod
    def guess_string(value):
        assert type(value) is str

    @staticmethod
    def guess_type(value):
        typ = type(value)
        allow_list = {
            bool: xcfg_type.bool,
            int: xcfg_type.number,
            float: xcfg_type.float,
            list: xcfg_type.array,
            str: xcfg_type.string,
        }
        assert typ in allow_list.keys()
        # if typ is str:
        #     return xcfg_type.guess_string(value)
        return xcfg_type.guess_string(value) if typ is str else allow_list[typ]
        # if typ is bool:
        #     return xcfg_type.bool
        # if typ is int:
        #     return xcfg_type.number
        # if typ is float:
        #     return xcfg_type.float
        # if typ is list:
        #     return xcfg_type.array
        # # datetime/date/time/timezone
        # if typ is str:
        #     return xcfg_type.string


# name = value ; <(type, default)> description <(type, default)>
# 应该主要通过猜测实现，注释和属性应该前后可选，可以前+后
# 注释需支持多行与自动换行
# 连接符可选
class xcfg_item(xcfg_name):
    # TODO: 断言类型，猜测类型
    def __init__(self, name, value, **kwargs):
        # uuid = kwargs.pop('uuid', 0)
        xtype = kwargs.pop(
            'type',
            xcfg_item.guess_type(value))  # 当type存在时无需猜测，但是需要确保type为xcfg_type对象
        default = kwargs.pop('default', None)
        description = kwargs.pop('description', None)
        # self.__uuid = uuid
        self.__xname = xcfg_name(name)
        self.__xtype = xtype
        self.__value = value
        self.__default = default  # default
        self.__description = description  # description

    def __repr__(self):
        return f"{self.__xname.human} = {self.__value}"

    def __str__(self):
        return f"{self.__xname.human} = {self.__value}"
