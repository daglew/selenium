import unittest


class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*-" * 20)
        print("Class 2 -> class level setUp.")
        print("*-" * 20)

    def setUp(self):
        print("Class 2 -> setUp.")

    def test_class2_method_a(self):
        print("Running class 2 -> method A.")

    def test_class2_method_b(self):
        print("Running class 2 -> method B.")

    def tearDown(self):
        print("Class 2 -> tearDown.")

    @classmethod
    def tearDownClass(cls):
        print("*-" * 20)
        print("Class 2 -> class level tearDown.")
        print("*-" * 20)


if __name__ == '__main__':
    unittest.main(verbosity=2)

