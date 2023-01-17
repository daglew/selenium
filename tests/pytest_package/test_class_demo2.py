import pytest
from tests.pytest_package.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestClassDemo:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.abc = SomeClassToTest(value=10)

    def test_methoda(self):
        result = self.abc.sum_numbers(2, 8)
        assert result == 20
        print("Running method a.")

    def test_methodb(self):
        print("Running method b.")

