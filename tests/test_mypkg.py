import unittest
from mypkgcolav1 import pkg
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pkg = pkg.mypkg(123)

    def test_var(self):
        self.assertEqual(self.pkg.get(), 123)

if __name__ == '__main__':
    unittest.main()