import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/fl/firefox.chrome/chromedriver_79.exe')
driver.get('http://suninjuly.github.io/explicit_wait2.html')

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

button = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button = driver.find_element_by_id('book').click()

x = driver.find_element_by_id('input_value').text
x = calc(x)
driver.find_element_by_id('answer').send_keys(x)
driver.find_element_by_id('solve').click()


time.sleep(3)
driver.close()

