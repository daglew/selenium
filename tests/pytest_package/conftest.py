import pytest


@pytest.fixture
def setUp():
    print("Runing conftest demo1 before every method setup.")
    yield
    print("Runing conftest demo1 before every method tearDown.")


@pytest.fixture(scope="module")
def one_time_setUp():
    print("Runing conftest demo_one_time before every method setup.")
    yield
    print("Runing conftest demo_one_time before every method tearDown.")

