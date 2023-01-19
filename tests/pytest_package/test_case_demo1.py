import pytest


@pytest.fixture()
def setup():
    print("Runing once before every method.")


def test_method_a(setup):
    print("Runing method A.")


def test_method_b(setup):
    print("Runing method B.")
