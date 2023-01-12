"""
py.test test_mod.py  #run tests in module
py.test somepath  #run all tests below somepath
py test test_module.py::test_method  #only run test_method in test_module

-s to print statements
-v verbose

"""

import pytest


@pytest.fixture()
def setup():
    print(" Runing demo3 setup.")
    yield
    print(" Runing demo3 teardown.")


def test_demo3_methoda(setup):
    print(" Runing demo3 method A.")


def test_demo3_methodb(setup):
    print(" Runing demo3 method B.")

