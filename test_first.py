from .pages.main_page import MainPage
from .pages.tensor_page import TensorPage
from .pages.contact_page import ContactPage
from .pages.about_page import AboutPage


class TestFirst:
    link = 'https://sbis.ru/'
    about_url = 'https://tensor.ru/about'

    def test_go_to_contacts(self, browser):
        page_main = MainPage(browser, self.link)
        page_main.open()
        page_main.go_to_contacts()

    def test_go_to_tensor(self, browser):
        page_contact = ContactPage(browser, browser.current_url)
        page_contact.go_to_tensor()

    def test_check_block(self, browser):
        tesor_page = TensorPage(browser, browser.current_url)
        tesor_page.should_be_block_people()
        

    def test_go_to_about(self, browser):
        tesor_page = TensorPage(browser, browser.current_url)
        tesor_page.go_to_about()

    def test_check_url_size(self, browser):
        about_page = AboutPage(browser, browser.current_url)
        about_page.should_be_currect_url(self.about_url)
        about_page.should_be_currect_size()
