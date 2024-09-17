# pip install selenium
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.ifood.com.br/inicio')
sleep(3)

from selenium.webdriver.common.by import By
popup = driver.find_element(By.CLASS_NAME, 'marmita-modal__inner-content')
btn = popup.find_element(By.XPATH, '//button[@aria-label="Usar minha localização"]')
btn.click()

sleep(2)
form = driver.find_element(By.TAG_NAME, 'form')
input1 = form.find_element(By.TAG_NAME, 'input')
input1.send_keys('pizza')

from selenium.webdriver.common.keys import Keys
input1.send_keys(Keys.ENTER)

sleep(3)
nav_bar = driver.find_element(By.TAG_NAME, 'ul')
filter_btn = nav_bar.find_element(By.XPATH, '//button[@class="toggle-chip toggle-chip--baseline"]')
filter_btn.click()

sleep(3)
filter_section = driver.find_element(By.CLASS_NAME, 'cardstack-full-filter__grid')
filter_list = filter_section.find_element(By.XPATH, '//div[@class="full-grid__container"]')
taxa_div_list = filter_list.find_elements(By.TAG_NAME, 'button')
taxa_div_list[1].click()

sleep(3)
filter_btn_div = filter_section.find_element(By.CLASS_NAME, 'cardstack-full-filter__filter')
filter_apply_btn = filter_btn_div.find_element(By.TAG_NAME, 'button')
filter_apply_btn.click()

sleep(10)
driver.close()
