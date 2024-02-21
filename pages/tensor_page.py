from .base_page import BasePage
from selenium.webdriver.common.by import By


class TensorPage(BasePage):
    def should_be_block_people(self):
        assert self.is_element_present(By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content'), "Failde: block missing"


    def go_to_about(self):
        about = self.browser.find_element(By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content p:nth-child(4) a')
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", about)
        about.click()
    