from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Вариант 1: Если используете ручной путь к chromedriver.exe
service = Service('C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_5.Знакомство с Selenium\\Хром драйвер 2\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# ИЛИ (выберите только один вариант — либо выше, либо ниже)

# Вариант 2: Если хотите автоматическую загрузку ChromeDriver (рекомендуется)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

sleep(50)
