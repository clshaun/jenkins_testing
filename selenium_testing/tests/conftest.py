import pytest

from selenium_testing.pages.page_initializers import AppPages


@pytest.fixture
def pages(py):
    return AppPages(py)


