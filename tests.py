import unittest
from brackets import check_brackets

class TestBracketsMethod(unittest.TestCase):

    def tests_method(self):
        self.assertTrue(check_brackets('[({})]'))
        self.assertTrue(check_brackets('[{(({{[]}}))}]'))
        self.assertTrue(check_brackets(''))
        self.assertFalse(check_brackets('[)'))
        self.assertFalse(check_brackets('[[]'))
        self.assertFalse(check_brackets(']['))
        self.assertFalse(check_brackets('abcd'))