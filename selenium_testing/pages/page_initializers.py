from pylenium.driver import Pylenium

from selenium_testing.pages.add_remove_elements_page import AddRemoveElementsPage
from selenium_testing.pages.home_page import HomePage
from selenium_testing.pages.login_page import LoginPage


class AppPages:

    def __init__(self, py: Pylenium):
        self.py = py
        self.login = LoginPage(py)
        self.home = HomePage(py)
        self.add_remove = AddRemoveElementsPage(py)
