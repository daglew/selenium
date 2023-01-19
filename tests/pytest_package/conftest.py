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
# """
# command line
# """
#
# @pytest.fixture()
# def setup():
#     print("Running method level setup.")
#     yield
#     print("Running method level teardown.")
#
#
# @pytest.fixture(scope="module")
# def one_time_setup(browser, ostype):
#     print("Running one_time_setup.")
#     if browser == "firefox":
#         print("Running tests on FF.")
#     else:
#         print("Running tests on chrome.")
#     yield
#     print("Running one time teardown.")
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--ostype", help="Type of operating system.")
#
#
# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture(scope="session")
# def ostype(request):
#     return request.config.getoption("--ostype")

"""
class to test
"""


@pytest.yield_fixture()
def setup():
    print("Running method level setup.")
    yield
    print("Running method level teardown.")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("Running one_time_setup.")
    if browser == "firefox":
        value = 10
        print("Running tests on FF.")
    else:
        value = 10
        print("Running tests on chrome.")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print("Running one time teardown.")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help="Type of operating system.")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--ostype")



