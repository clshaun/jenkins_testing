import time

from selenium_testing.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, py):
        super().__init__(py)

    def login_to_the_gram(self, username, password):
        self.py.delete_all_cookies()
        self.py.visit("https://www.instagram.com")
        self.py.get("input[name='username']").type(username)
        self.py.get("input[name='password']").type(password)
        self.py.getx("//button[@type='submit']").click()
        time.sleep(150)
