from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time
import math


driver = WebDriver(executable_path='C:/fl/firefox.chrome/chromedriver_79.exe')
driver.implicitly_wait(2)
driver.get('http://suninjuly.github.io/selects1.html')

driver.execute_script('document.title="Script executing";')
#
# def calc(nu1, nu2):
#     return str(int(nu1) + int(nu2))
#
# try:
#     nu1 = driver.find_element_by_id('num1').text
#     nu2 = driver.find_element_by_id('num2').text
#
#     y = calc(nu1, nu2)
#
#     fiel = driver.find_element_by_class_name('custom-select').click()
#
#     select = Select(driver.find_element_by_tag_name("select"))
#     select.select_by_value(y)  # ищем элемент с текстом "Python"
#
#     submit = driver.find_element_by_tag_name('[type="submit"]').click()
#
#
#
#
# finally:
#     print(y)
#     time.sleep(5)
#     driver.close()