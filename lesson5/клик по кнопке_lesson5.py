from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(1, 6):
    driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
    sleep(2)  # Добавляем паузу для обновления списка элементов

added_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(len(added_buttons))

sleep(5)