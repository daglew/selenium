import unittest


class DemoTestCase(unittest.TestCase):
    def setUp(self):
        print("I run once before each test.")

    def method_a_test(self):
        print("Run method A.")

    def method_b_test(self):
        print("Run method B.")

    def tearDown(self):
        print("I run after every test.")


if __name__ == '__main__':
    unittest.main(verbosity=2)

