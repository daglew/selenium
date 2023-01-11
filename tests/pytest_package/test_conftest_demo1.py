import pytest


@pytest.fixture
def setUp():
    print("Runing conftest demo1 before every method setup.")
    yield
    print("Runing conftest demo1 before every method tearDown.")


def test_demo1_method_a(setUp):
    print("Runing conftest demo1 method a.")


def test_demo1_method_b(setUp):
    print("Runing conftest demo1 method B.")
