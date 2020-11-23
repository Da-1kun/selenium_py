from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import screenshot as scs

DRIVER_PATH = './chromedriver'


def __init_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    return webdriver.Chrome(chrome_options=options,
                            executable_path=DRIVER_PATH)


if __name__ == '__main__':
    driver = __init_driver()

    driver.get('https://selenium-python.readthedocs.io/')
    scs.take_screenshot(driver, 'full_screenshot')

    driver.close()
