from selenium.webdriver.common.keys import Keys

def

def new_searchers(browser, text):
    search = browser.find_element_by_name('q')

    browser.find_element_by_name('q').clear()
    search.send_keys(text)
    search.send_keys(Keys.RETURN)