import pytest


@pytest.fixture
def setup():
    print("Runing conftest demo1 before every method setup.")
    yield
    print("Runing conftest demo1 before every method teardown.")


@pytest.fixture(scope="module")
def one_time_setup():
    print("Runing conftest demo_one_time before every method setup.")
    yield
    print("Runing conftest demo_one_time before every method teardown.")

