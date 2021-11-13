from .pages.main_page import MainPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer '

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#registration_link")
    login_link.click()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

