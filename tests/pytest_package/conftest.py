import pytest


# @pytest.fixture
# def setup():
#     print("Runing conftest demo1 before every method setup.")
#     yield
#     print("Runing conftest demo1 before every method teardown.")
#
#
# @pytest.fixture(scope="module")
# def one_time_setup():
#     print("Runing conftest demo_one_time before every method setup.")
#     yield
#     print("Runing conftest demo_one_time before every method teardown.")
#

@pytest.fixture()
def setup():
    print("Running method level setup.")
    yield
    print("Running method level teardown.")


@pytest.fixture(scope="module")
def one_time_setup(browser, ostype):
    print("Running one time setup.")
    if browser == "firefox":
        print("Running tests on FF.")
    else:
        print("Running tests on chrome.")
    yield
    print("Running one time teardown.")


def pytest_add_option(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help="Type of operating system.")


@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")

