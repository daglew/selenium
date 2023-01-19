import pytest


@pytest.fixture()
def setup():
    print(" Runing demo2 setup.")
    yield
    print(" Runing demo2 teardown.")


def test_demo2_methoda(setup):
    print(" Runing demo2 method A.")


def test_demo2_methodb(setup):
    print(" Runing demo2 method B.")

