import pytest
from configurations.config import Config
from selenium import webdriver


def pytest_addoption(parser):
    """
    Adds command line flags: --env, --browser --local, when program executed from command line.
    in case no value supplied, default values would be stored (qa, chrome, False in accordance).
    """
    parser.addoption(
        "--env", action="store", default="qa", help="Environment to run the tests on."
    )
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser name."
    )


@pytest.fixture("session")
def env(request):
    """
    :param request: pytest request object
    :return: the value of --env flag
    """
    return request.config.getoption("--env")


@pytest.fixture("session")
def browser_name(request):
    """
    :param request: pytest request object
    :return: the value of --browser flag
    """
    return request.config.getoption("--browser")


@pytest.fixture("session")
def config(env):
    """
    :param env: environment string supplied from command line
    :return: config object with system configurations
    """
    return Config(env)


@pytest.fixture("session")
def desired_capabilities(browser_name):
    """
    :param browser_name:
    :return: a desired_capabilities object with the browser name from the command line or default
    if not specified.
    """
    capabilities = {"browserName": browser_name,
                    "version": "",
                    "platform": "ANY"}
    return capabilities


@pytest.fixture
def browser(browser_name, config, desired_capabilities):
    """
    :param browser_name: The name of the browser to execute tests
    :param config: system configurations object
    :param desired_capabilities: desired capabilities object to create instance of remote driver
    :return: an instance of a remote driver object
    """
    driver = webdriver.Remote(command_executor="http://hub:4444/wd/hub", desired_capabilities=desired_capabilities)
    driver.implicitly_wait = config.time_out
    driver.maximize_window()
    yield driver
    driver.quit()
