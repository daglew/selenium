import pytest

@pytest.fixture()
def setUp():
    print(" Runing once before every method.")
    yield
    print(" Runing once after every method.")


def test_method_a(setUp):
    print(" Runing method A.")


def test_method_b(setUp):
    print(" Runing method B.")

