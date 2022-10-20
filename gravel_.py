from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selectors import SELECTORS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class gravel:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(
            executable_path='./utils/chromedriver.exe', options=chrome_options)
        self.keys = Keys

    def chain(self):
        return ActionChains(self.driver)

    def wait4element(self, selector, sleep=10):
        return WebDriverWait(self.driver, sleep).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))

    def getElement(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, SELECTORS.get(selector))

    def driver(self):
        return self.driver

    def keys(self):
        return Keys

    def close(self):
        return self.driver.close()


if __name__ == '__main__':
    gravel()
