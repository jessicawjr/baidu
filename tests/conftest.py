import logging
from unittest import mock

import pytest
from selenium import webdriver

from baidu.homepage import Homepage

logging.disable(logging.ERROR)


@pytest.fixture(scope="function")
def driver_mock():
    """
    Returns a mock selenium driver object
    """
    return mock.create_autospec(webdriver.Firefox)


@pytest.fixture(scope="function")
def homep(driver_mock):
    return Homepage(driver_mock)