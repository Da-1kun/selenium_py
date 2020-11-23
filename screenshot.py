def __screen_width(driver): return driver.execute_script(
    'return screen.width'
)


def __full_page_height(driver): return driver.execute_script(
    'return document.body.clientHeight')


def take_screenshot(driver, store_path):
    driver.set_window_size(__screen_width(driver), __full_page_height(driver))
    driver.find_element_by_tag_name('body').screenshot(f'{store_path}.png')
