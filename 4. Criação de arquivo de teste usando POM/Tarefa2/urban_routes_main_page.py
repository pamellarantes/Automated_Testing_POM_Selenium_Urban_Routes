from selenium.webdriver.common.by import By


# Definição da classe da página, dos localizadores e do método na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = ...
    TO_LOCATOR = ...
    PERSONAL_OPTION_LOCATOR = ...
    CARSHARING_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = ...
    CAMPING_LOCATOR = ...
    AUDI_TEXT_LOCATOR = ...

    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver

    def enter_from_location(self, from_text):
        # Inserir De
        ...

    def enter_to_location(self, to_text):
        # Inserir Para
        ...

    def click_personal_option(self):
        # Clicar Personal
        ...

    def click_carsharing_icon(self):
        # Clique no ícone Carsharing
        ...

    def click_book_button(self):
       # Clique no botão Reservar
        ...

    def click_camping(self):
        # Clique em Camping
        ...

    def get_audi_text(self):
        # Retornar o texto "Audi"
        ...
