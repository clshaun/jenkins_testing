import time

from selenium.common.exceptions import ElementNotInteractableException
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

    # region WordPress Login
    def login_to_wordpress(self, username, password):
        self.py.delete_all_cookies()
        self.py.visit("https://wordpress.com/me")
        self.py.get("#usernameOrEmail").type(username)
        self.click_element(xpath="//button[contains(text(),'Continue')]")
        try:
            self.py.get("#password").type(password)
        except ElementNotInteractableException:
            time.sleep(1.5)
            self.py.get("#password").type(password)
        self.click_element(xpath="//button[contains(text(),'Log In')]", page_redirect=True)
    # endregion WordPress Login
