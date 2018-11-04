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

    ids = browser.find_elements_by_xpath("//div[@class='sbqs_c']")

    for item in ids:
        print(item.text)
