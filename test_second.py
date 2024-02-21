import time
from .pages.main_page import MainPage
from .pages.tensor_page import TensorPage
from .pages.contact_page import ContactPage
from .pages.about_page import AboutPage

def test_second(browser):
    link = 'https://sbis.ru/'
    old_region = 'Новосибирск'
    new_region = 'Камчатский край'
    change_url = '41-kamchatskij-kraj'
    page_main = MainPage(browser, link)
    page_main.open()
    page_main.go_to_contacts()
    
    page_contact = ContactPage(browser, browser.current_url)
    page_contact.check_region(old_region)
    page_contact.change_region(new_region)

    page_contact.check_region(new_region)
    page_contact.check_title_region(new_region)
    page_contact.check_url_region(change_url)

