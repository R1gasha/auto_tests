from .base_page import BasePage
from selenium.webdriver.common.by import By


class TensorPage(BasePage):
    def should_be_block_people(self):
        assert self.is_element_present(By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content'), "Failde: block missing"