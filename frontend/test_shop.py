import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
URL = 'https://testqastudio.me/'

def test_product_view_sku():
    """
    Test case WERT-1
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    driver.get(url=URL)
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='post-11341']")
    element.click()
    art = driver.find_element(By.CLASS_NAME, value="sku")
    assert art.text == "C0MSSDSUM7", "Упси-дупси чтото пошло не так(("
    assert True, ""