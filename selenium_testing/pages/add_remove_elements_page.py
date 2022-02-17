import random

from selenium_testing.pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):

    def __init__(self, py):
        super().__init__(py)

    def goto(self):
        self.py.visit("https://the-internet.herokuapp.com/add_remove_elements/")

    def click_add_element(self):
        self.click_element(xpath="//button[contains(text(),'Add Element')]")

    def create_random_amount_of_element_boxes(self):
        random_amount = random.randint(1, 30)
        for i in range(random_amount):
            self.click_add_element()
        return random_amount

    def get_all_new_elements(self):
        els = self.py.find("button.added-manually")
        return els

    def delete_all_elements(self):
        els = self.py.find("button.added-manually")
        for i in els:
            i.click()
