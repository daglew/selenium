import pytest


@pytest.fixture()
def setUp():
    print(" Runing demo2 setUp.")
    yield
    print(" Runing demo2 tearDown.")


def test_demo2_methoda(setUp):
    print(" Runing demo2 method A.")


def test_demo2_methodb(setUp):
    print(" Runing demo2 method B.")

