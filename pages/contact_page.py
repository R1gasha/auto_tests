from .base_page import BasePage
from selenium.webdriver.common.by import By

class ContactPage(BasePage):
    def go_to_tensor(self):
        contact_link = self.browser.find_element(By.CSS_SELECTOR, "div.sbisru-Contacts__border-left a")
        contact_link.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
