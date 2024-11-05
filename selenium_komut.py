from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
url="https://www.youtube.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

googleArama=driver.find_element(By.NAME,"search_query")
googleArama.send_keys("python")
time.sleep(1)
googleArama.send_keys(Keys.ENTER)
time.sleep(2)

#dersbasliklari=driver.find_elements(By.ID,"title")
dersbasliklari=driver.find_elements(By.XPATH,'//*[@id="title"]')
for baslik in dersbasliklari:
    print(baslik.text)

time.sleep(2)
driver.quit()