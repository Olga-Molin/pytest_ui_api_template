#AuthPage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://trello.com/login"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, password: str):
        #Находим поле с логином. Передаем в него значение переменной email:
        self.__driver.find_element(By.CSS_SELECTOR, "#user").send_keys(email)

        #Кликаем на кнопку «Продолжить»:
        self.__driver.find_element(By.CSS_SELECTOR, "#login").click()

        #Дожидаемся, когда поле «Введите пароль» отрисуется:
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg[role=presentation]")))

        #Находим поле «Введите пароль», передаем ему значение переменной password:
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

        #Находим кнопку «Войти» и нажимаем на нее
        self.__driver.find_element(By.CSS_SELECTOR, "#login_submit").click()

     #Возвращаем текущий URL
    def get_current_url(self):
         return self.__driver.current_url