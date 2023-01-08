import unittest


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*-" * 20)
        print("Class 1 -> class level setUp.")
        print("*-" * 20)

    def setUp(self):
        print("Class 1 -> setUp.")

    def test_class1_method_a(self):
        print("Running class 1 -> method A.")

    def test_class1_method_b(self):
        print("Running class 1 -> method B.")

    def tearDown(self):
        print("Class 1 -> tearDown.")

    @classmethod
    def tearDownClass(cls):
        print("*-" * 20)
        print("Class 1 -> class level tearDown.")
        print("*-" * 20)


if __name__ == '__main__':
    unittest.main(verbosity=2)

