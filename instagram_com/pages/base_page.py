from pylenium.driver import Pylenium


class BasePage:

    def __init__(self, py: Pylenium):
        self.py = py
