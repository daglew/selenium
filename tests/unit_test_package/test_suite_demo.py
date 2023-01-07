import unittest
from tests.unit_test_package.test_class_1 import TestClass1
from tests.unit_test_package.test_class_2 import TestClass2

# get everything tests from TestClass1 and TestClass2
t_c_1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
t_c_2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# connection a test TestClass1 and TestClass2
combining_tests = unittest.TestSuite([t_c_1, t_c_2])

unittest.TextTestRunner(verbosity=2).run(combining_tests)

