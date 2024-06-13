from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ждем появления модального окна
wait.until(EC.visibility_of_element_located((By.ID, "modal")))
# Кликаем на кнопку закрытия
driver.find_element(By.CSS_SELECTOR, "#modal .modal-footer button").click()

sleep(3)