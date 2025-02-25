from selenium.webdriver.common.by import By


# Definição da classe da página, dos localizadores e do método na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    BIKE_ICON_LOCATOR = ...
    BIKE_TEXT_LOCATOR = ...

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
        ...

    def click_bike_icon(self):
        # Clicar no ícone Bicicleta
        ...

    def get_bike_text(self):
        # Retornar o texto "Bicicleta"
        ...
