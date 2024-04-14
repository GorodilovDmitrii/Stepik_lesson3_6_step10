from selenium.webdriver.common.by import By


def test_item_has_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(5)
    add_to_basket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket[0]
