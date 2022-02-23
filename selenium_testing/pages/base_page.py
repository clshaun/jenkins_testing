import time
from contextlib import contextmanager

from pylenium.driver import Pylenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of


class BasePage:

    def __init__(self, py: Pylenium):
        self.py = py

    @contextmanager
    def wait_for_page_load_on_click(self, el_to_be_stale=None, timeout=10):
        if el_to_be_stale:
            old_page = el_to_be_stale
        else:
            old_page = self.py.webdriver.find_element(By.TAG_NAME, 'html')
        yield
        self.py.wait(timeout).until(staleness_of(old_page))
        time.sleep(1)

    def click_element(self, xpath=None, css=None, timeout=5, page_redirect=False):
        if xpath:
            el = self.py.getx(xpath, timeout)
        elif css:
            el = self.py.get(css, timeout)

        if page_redirect:
            with self.wait_for_page_load_on_click(el):
                el.click()
        else:
            el.click()
        return el

    def get_el_attribute(self, xpath=None, css=None, attribute=None, timeout=10):
        if xpath:
            el = self.py.getx(xpath, timeout)
            value = el.get_attribute(attribute)
        elif css:
            el = self.py.get(css, timeout)
            value = el.get_attribute(attribute)

        return value
