from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from view.google_views import new_searchers

class HandlerSearchers:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def searchers(self):
        print('Iniciando as pesquisas...')
        new_searchers(browser=self.browser, text='')