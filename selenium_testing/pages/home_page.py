import os.path
import re
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium_testing.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, py):
        super().__init__(py)

    # region Heroku App
    def goto_heroku_home_page(self):
        self.py.visit("https://the-internet.herokuapp.com/")


    # endregion Heroku App

    # region WordPress site
    def goto_wordpress_site(self):
        self.py.visit("https://wordpress.com/me")

    def fill_out_first_name(self, first_name):
        return self.py.get("#first_name").clear().type(first_name)

    def fill_out_last_name(self, last_name):
        return self.py.get("#last_name").clear().type(last_name)

    def fill_out_display_name(self, display_name):
        return self.py.get("#display_name").clear().type(display_name)

    def fill_out_about_me(self, about_me_text):
        return self.py.get("#description").clear().type(about_me_text)

    def left_side_profile_username(self, search_value):
        return self.py.getx(f"//h2[contains(text(),'{search_value}')]").text()

    def get_all_text_values(self):
        text_values = dict()
        text_values["first_name"] = self.get_el_attribute(css="#first_name", attribute='value')
        text_values["last_name"] = self.get_el_attribute(css="#last_name", attribute='value')
        text_values["display_name"] = self.get_el_attribute(css="#display_name", attribute='value')
        text_values["about_me"] = self.py.get("#description").text()

        return text_values

    def fill_out_profile_text_boxes(self, **profile):
        self.fill_out_first_name(profile['first_name'])
        self.fill_out_last_name(profile['last_name'])
        self.fill_out_display_name(profile['display_name'])
        self.fill_out_about_me(profile['about_me'])

    def change_profile_picture(self):
        path = os.path.dirname(__file__).split("pages")[0]
        self.py.getx("//body/form[1]/input[1]").type(f"{path}/assets/bender.jpeg")

    def click_add_profile_links(self, link_to_follow="Add URL"):
        add_url_xpath = "//button[contains(text(),'Add URL')]"
        add_wordpress_site_xpath = "//button[contains(text(),'Add WordPress Site')]"

        self.click_element(xpath="//span[contains(text(),'Add')]")
        if link_to_follow == "Add URL":
            self.py.getx(add_url_xpath).should().be_visible()
            self.click_element(xpath=add_url_xpath)
        elif link_to_follow == "Add Wordpress Site":
            self.py.getx(add_wordpress_site_xpath).should().be_visible()
            self.click_element(xpath=add_wordpress_site_xpath)

    def fill_out_add_url_section(self, url, description, submit=True):
        self.py.getx("//input[@name='value']").type(url)
        self.py.getx("//input[@name='title']").type(description)

        if submit and self.py.findx("//button[contains(text(),'Add Site')]"):
            self.click_element(xpath="//button[contains(text(),'Add Site')]")

    def fill_out_and_cancel_url_section(self, url, description):
        self.fill_out_add_url_section(url, description, submit=False)
        self.click_element(xpath="//button[contains(text(),'Cancel')]")
        return self.get_profile_links()

    def get_profile_links(self):
        return self.py.getx("//div[@class='card'//div").text()

    def del_profile_links(self):
        delete_els = self.py.find("button.button.profile-link__remove.is-borderless")
        for x in range(len(delete_els)):
            for y in delete_els:
                try:
                    y.click()
                except StaleElementReferenceException:
                    continue

    def save_profile(self):
        count = 0
        self.click_element(xpath="//button[contains(text(),'Save profile details')]")
        while not self.py.getx("//span[contains(text(),'Settings saved successfully!')]").is_displayed() and count < 5:
            time.sleep(1)
            count += 1

    def logout(self):
        self.click_element(xpath="//button[contains(text(),'Log out')]", page_redirect=True)

    # endregion WordPress site

    # region Random pages
    def goto_weather_site(self):
        self.py.visit("https://weathershopper.pythonanywhere.com/")
        temp = self.py.get("#temperature").text()
        temp = re.findall('[0-9]+', temp)
        return int(temp[0])

    def click_buy_moisturizers(self):
        self.py.getx("//button[contains(text(),'Buy moisturizers')]").click()
    # endregion Random pages