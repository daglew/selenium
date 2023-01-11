import pytest

@pytest.fixture
def setUp():
    print("Runing conftest demo1 before every method setup.")
    yield
    print("Runing conftest demo1 before every method tearDown.")

