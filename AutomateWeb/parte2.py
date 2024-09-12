# pip install selenium
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.ifood.com.br/inicio')

sleep(3)
popup = driver.find_element(By.CLASS_NAME, 'marmita-modal__inner-content')
btn = popup.find_element(By.XPATH, '//button[@aria-label="Usar minha localização"]')
btn.click()

# sleep(3)
# wait = WebDriverWait(driver, timeout=2)
# alert = wait.until(lambda d: d.switch_to.alert)
# text = alert.text
# alert.accept()

sleep(3)
form = driver.find_element(By.TAG_NAME, 'form')
input1 = form.find_element(By.TAG_NAME, 'input')
input1.send_keys('pizza')
input1.send_keys(Keys.ENTER)

sleep(3)
driver.close()

