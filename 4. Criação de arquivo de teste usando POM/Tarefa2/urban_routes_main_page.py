from selenium.webdriver.common.by import By

# Definição da classe da página, dos localizadores e do método na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    CARSHARING_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    CAMPING_LOCATOR = (By.XPATH, '//div[contains(text(),"Camping")]')
    AUDI_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Audi A3 Sedã")]')
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '(//div[contains(text(),"Adicionar carteira de motorista")])[2]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Add"]')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(), "Obrigado")]')
    DURATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Duração")]')

    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver

    def enter_from_location(self, from_text):
        # Inserir De
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Inserir Para
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_personal_option(self):
        # Clicar Personal
        self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR).click()

    def click_carsharing_icon(self):
        # Clique no ícone Carsharing
        self.driver.find_element(*self.CARSHARING_ICON_LOCATOR).click()

    def click_book_button(self):
        # Clique no botão Reservar
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def click_camping(self):
        # Clique em Camping
        self.driver.find_element(*self.CAMPING_LOCATOR).click()

    def get_audi_text(self):
        # Retornar o texto "Audi"
        return self.driver.find_element(*self.AUDI_TEXT_LOCATOR).text
