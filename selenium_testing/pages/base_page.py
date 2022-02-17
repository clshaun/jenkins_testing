from pylenium.driver import Pylenium


class BasePage:

    def __init__(self, py: Pylenium):
        self.py = py

    def click_element(self, xpath=None, css=None, timeout=5):
        if xpath:
            el = self.py.getx(xpath, timeout)
            el.click()
        elif css:
            el = self.py.get(css, timeout)
            el.click()
        return el
