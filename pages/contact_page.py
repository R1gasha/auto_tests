from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(BasePage):
    def go_to_tensor(self):
        contact_link = self.browser.find_element(By.CSS_SELECTOR, "div.sbisru-Contacts__border-left a")
        contact_link.click()
        self.browser.switch_to.window(self.browser.window_handles[1])


    def check_region(self, check_city):
        region = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".s-Grid-col + .s-Grid-col--xm12 > .sbis_ru-Region-Chooser > .sbis_ru-Region-Chooser__text"), check_city)
        )
        assert self.is_element_present(By.CSS_SELECTOR, "#contacts_list .sbis_ru-container .sbisru-Contacts-List__col"), "Failde: missing block contacts"
        assert region, "Failed: uncorrect region"

    
    def change_region(self, region):
        old_region = self.browser.find_element(By.CSS_SELECTOR, ".s-Grid-col + .s-Grid-col--xm12 > .sbis_ru-Region-Chooser > .sbis_ru-Region-Chooser__text")
        old_region.click()
        new_region = self.browser.find_element(By.CSS_SELECTOR, f'[title="{region}"]')
        new_region.click()

    def check_url_region(self, region):
        assert self.check_url(region), "Failed: uncorrect url"

    def check_title_region(self, region):
        assert self.check_title(region), "Failed: uncorrect title"
