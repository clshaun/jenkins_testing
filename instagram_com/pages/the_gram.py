from pylenium.driver import Pylenium

from instagram_com.pages.home_page import HomePage
from instagram_com.pages.login_page import LoginPage


class TheGram:

    def __init__(self, py: Pylenium):
        self.py = py
        self.login = LoginPage(py)
        self.home = HomePage(py)