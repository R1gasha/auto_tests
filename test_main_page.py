import time
from .pages.main_page import MainPage
from .pages.tensor_page import TensorPage
from .pages.contact_page import ContactPage


def test_go_to_contacts(browser):
    link = 'https://sbis.ru/'
    page_main = MainPage(browser, link)
    page_main.open()
    page_main.go_to_contacts()
    
    page_contact = ContactPage(browser, browser.current_url)
    page_contact.go_to_tensor()

    tesor_page = TensorPage(browser, browser.current_url)
    tesor_page.should_be_block_people()