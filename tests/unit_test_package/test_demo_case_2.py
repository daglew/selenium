import unittest


class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*-" * 20)
        print("I will run only once before all tests")
        print("*-" * 20)

    def setUp(self):
        print("I run once before each test.")

    def test_method_a(self):
        print("Run method A.")

    def test_method_b(self):
        print("Run method B.")

    def tearDown(self):
        print("I run after every test.")

    @classmethod
    def tearDownClass(cls):
        print("*-" * 20)
        print("I will run only once after all tests")
        print("*-" * 20)

if __name__ == '__main__':
    unittest.main(verbosity=2)

