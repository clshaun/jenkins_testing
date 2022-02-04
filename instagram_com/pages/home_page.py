import re
import time

from instagram_com.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, py):
        super().__init__(py)

    def goto_weather_site(self):
        self.py.visit("https://weathershopper.pythonanywhere.com/")
        temp = self.py.get("#temperature").text()
        temp = re.findall('[0-9]+', temp)
        return int(temp[0])

    def click_buy_moisturizers(self):
        self.py.getx("//button[contains(text(),'Buy moisturizers')]").click()