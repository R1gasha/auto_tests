from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_contacts(self):
        contact_link = self.browser.find_element(By.CSS_SELECTOR, "div.sbisru-Header__container ul li:nth-child(2) a")
        contact_link.click()