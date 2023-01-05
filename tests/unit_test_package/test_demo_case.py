import unittest


class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print("I run once before each test.")

    def test_method_a(self):
        print("Run method A.")

    def test_method_b(self):
        print("Run method B.")

    def tearDown(self):
        print("I run after every test.")


if __name__ == '__main__':
    unittest.main(verbosity=2)

