from .pages.main_page import MainPage
from .pages.tensor_page import TensorPage
from .pages.contact_page import ContactPage
from .pages.about_page import AboutPage

class TestSecond:
    link = 'https://sbis.ru/'
    old_region = 'Новосибирск'
    new_region = 'Камчатский край'
    change_url = '41-kamchatskij-kraj'

    def test_go_to_contacts(self, browser):
        page_main = MainPage(browser, self.link)
        page_main.open()
        page_main.go_to_contacts()

    def test_check_region(self, browser):
        page_contact = ContactPage(browser, browser.current_url)
        page_contact.check_region(self.old_region)
        
    def test_change_region(self, browser):
        page_contact = ContactPage(browser, browser.current_url)
        page_contact.change_region(self.new_region)

    def test_chech_new_region(self, browser):
        page_contact = ContactPage(browser, browser.current_url)
        page_contact.check_region(self.new_region)
        page_contact.check_title_region(self.new_region)
        page_contact.check_url_region(self.change_url)


