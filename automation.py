import selenium
import chromedriver_binary
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

buscas_json = '{"google-me": ["Nextel","telefonia do futuro","selenium python"]}'
buscas = json.loads(buscas_json)

google_me = buscas["google-me"]

for busca in google_me:
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(busca)
    search.send_keys(Keys.RETURN)

    links = browser.find_elements_by_css_selector('div.r a:nth-child(1)')

    for link in links:
        href = link.get_attribute("href")
        print(href)

    browser.close()
