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

resultados = {}
google_me = buscas["google-me"]

for busca in google_me:
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(busca)
    search.send_keys(Keys.RETURN)

    links = browser.find_elements_by_css_selector('div.r a:first-child')

    link1 = links[0].get_attribute("href")
    link2 = links[3].get_attribute("href")
    link3 = links[6].get_attribute("href")

    print(link1)
    print(link2)
    print(link3)

    resultados.update({busca: [link1, link2, link3]})

    browser.close()
print(resultados)
resultados_json = json.dumps(resultados)
arquivo = open("resultados.json","w")
arquivo.write(resultados_json)
arquivo.close()
