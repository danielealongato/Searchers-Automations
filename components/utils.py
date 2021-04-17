import time


def take_picture(driver, name_photo):
    driver.save_screenshot(f'./image_screenshot/{name_photo}.png')
    print(f'Printscreen tirado, foto salva em "/image_screenshot/{name_photo}.png"')


def get_text_page(driver, link_page):
    message = driver.find_element_by_tag_name("body").text
    print(f"{message} referente ao site {link_page}")


def scrolling_page(driver):
    SCROLL_PAUSE_TIME = 0.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    print('Rolando a página...')
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
