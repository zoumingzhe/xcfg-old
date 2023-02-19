import unittest

from xcfg.obj.xcfg_item import xcfg_name, xcfg_type

# import mock


class test_xcfg_type(unittest.TestCase):

    def test_check_name(self):
        self.assertEqual(xcfg_type.bool.name, "bool")
        self.assertEqual(xcfg_type.string.name, "string")
        self.assertEqual(xcfg_type.number.name, "number")
        self.assertEqual(xcfg_type.float.name, "float")
        self.assertEqual(xcfg_type.array.name, "array")
        self.assertEqual(xcfg_type.check.name, "check")
        self.assertEqual(xcfg_type.choice.name, "choice")
        self.assertEqual(xcfg_type.datetime.name, "datetime")
        self.assertEqual(xcfg_type.date.name, "date")
        self.assertEqual(xcfg_type.time.name, "time")
        self.assertEqual(xcfg_type.timezone.name, "timezone")


class test_xcfg_name(unittest.TestCase):

    def setUp(self):
        self.human_cells = [
            ('xcfg', ('xcfg', )),
            ('xcfg.cell', ('xcfg', 'cell')),
            ('xcfg.__cell__.full-cell', ('xcfg', '__cell__', 'full-cell')),
            ('xcfg.__cell__.test.0k1', ('xcfg', '__cell__', 'test', '0k1')),
        ]
        self.assert_name = [
            '',
            '.',
            '..',
            '...',
            123,
            '1 2 3',
            '1.2 3',
            '1 2.3',
            'x.y&z',
            'x@y.z',
        ]
        self.assert_cell = [
            (),
            (1),
            ('1', 2),
            (1, '2'),
            ('1 2 3'),
            (1, '2', '3'),
            ('1', 2, '3'),
            ('1', '2', 3),
        ]

    def test_name(self):
        for _human_cells in self.human_cells:
            _name, _cell = _human_cells
            obj = xcfg_name(_name)
            self.assertEqual(str(obj), _name)
            self.assertEqual(repr(obj), _name)
            self.assertEqual(obj.human, _name)
            self.assertEqual(obj.cells, _cell)

    def test_join(self):
        for _human_cells in self.human_cells:
            _name, _cell = _human_cells
            obj = xcfg_name.join(*_cell)
            self.assertEqual(str(obj), _name)
            self.assertEqual(repr(obj), _name)
            self.assertEqual(obj.human, _name)
            self.assertEqual(obj.cells, _cell)

    def test_name_assert(self):
        for _name in self.assert_name:
            self.assertRaises(AssertionError, xcfg_name, _name)

    def test_join_assert(self):
        for _cell in self.assert_cell:
            self.assertRaises(AssertionError, xcfg_name.join, _cell)
