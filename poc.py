import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from components.utils import (take_picture,
                              get_text_page,
                              scrolling_page)

buscas_json = '{"google-me": ["Automação de processos", "Python", "Agilizando tarefas repetitivas"]}'
buscas = json.loads(buscas_json)

resultados = {}
google_me = buscas["google-me"]
browser = webdriver.Chrome()
browser.get('http://www.google.com')
browser.find_element_by_xpath('//*[@id="zV9nZe"]/div').click()
browser.fullscreen_window()

for busca in google_me:
    search = browser.find_element_by_name('q')

    browser.find_element_by_name('q').clear()
    search.send_keys(busca)
    search.send_keys(Keys.RETURN)

    scrolling_page(driver=browser)
    links = browser.find_elements_by_css_selector('div.g a:first-child')
    list_links = []
    for link in links:
        page = link.get_attribute("href")
        if len(list_links) <= 2:
            if not "google" in page:
                print(page)
                list_links.append(page)
        else:
            break

    for link_page in list_links:
        # open new blank tab
        browser.switch_to.window(browser.window_handles[0])
        browser.execute_script("window.open();")
        # switch to the new window which is second in window_handles array
        browser.switch_to.window(browser.window_handles[1])

        browser.get(link_page)

        scrolling_page(driver=browser)
        take_picture(driver=browser, name_photo=busca)
        get_text_page(driver=browser, link_page=link_page)

        browser.switch_to.window(browser.window_handles[1])
        browser.close()

        # resultados.update({busca: [link_page]})
    browser.switch_to.window(browser.window_handles[0])
browser.close()
print(resultados)
resultados_json = json.dumps(resultados)
arquivo = open("resultados.json", "w")
arquivo.write(resultados_json)
arquivo.close()
