from .base_page import BasePage
from selenium.webdriver.common.by import By

class AboutPage(BasePage):
    def should_be_currect_url(self):
        assert self.browser.current_url == 'https://tensor.ru/about', "Failed: Invalid URL"


    def should_be_currect_size(self):
        imgs = self.browser.find_elements(By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper img')
        img_size1 = (imgs[0].get_attribute("width"), imgs[0].get_attribute("height"))
        img_size2 = (imgs[1].get_attribute("width"), imgs[1].get_attribute("height"))
        img_size3 = (imgs[2].get_attribute("width"), imgs[2].get_attribute("height"))
        img_size4 = (imgs[3].get_attribute("width"), imgs[3].get_attribute("height"))
        assert img_size1 == img_size2 == img_size3 == img_size4, "Failed: uncurrect size"