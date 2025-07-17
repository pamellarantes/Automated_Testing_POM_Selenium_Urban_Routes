from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    SCOOTER_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]')
    SCOOTER_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Scooter")]')
    # O novo localizador de texto "Duração"
    DURATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Duração")]')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.FROM_LOCATOR))
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_personal_option(self):
        self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR).click()

    def click_scooter_icon(self):
        self.driver.find_element(*self.SCOOTER_ICON_LOCATOR).click()

    def get_scooter_text(self):
        return self.driver.find_element(*self.SCOOTER_TEXT_LOCATOR).text

    # O novo metodo retornando o texto "Duração"
    def get_duration_text(self):
        return self.driver.find_element(*self.DURATION_TEXT_LOCATOR).text

    # Etapa para inserir os locais "De" e "Para"
    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)