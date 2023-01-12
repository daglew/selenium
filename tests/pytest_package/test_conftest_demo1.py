import pytest


@pytest.fixture
def setup():
    print("Runing conftest demo1 before every method setup.")
    yield
    print("Runing conftest demo1 before every method teardown.")


def test_demo1_method_a(setup):
    print("Runing conftest demo1 method a.")


def test_demo1_method_b(setup):
    print("Runing conftest demo1 method B.")
