from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage


# Crie uma classe para ambos os testes
class TestUrbanRoutes:

    def test_carsharing_personal_camping_option(self):
        driver = webdriver.Chrome()
        driver.get('https://cnt-784b233b-3492-4228-8423-83e3047817c1.containerhub.tripleten-services.com')

        # Crie uma instância da classe de página
        urban_routes_page = UrbanRoutesPage(driver)

        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        driver.implicitly_wait(3)

       # Escolha a etapa do carro de camping para inserir "De", "Para" e clicar em "personal_option",
        # "carsharing_icon", "book_button", e "camping"
        ...

        # Verifique se o texto exibe "Audi A3 Sedã"
        actual_value = urban_routes_page.get_audi_text()
        expected_value = "Audi A3 Sedã"
        assert expected_value in actual_value, f"Esperado '{expected_value}', mas recebeu '{actual_value}'"
        driver.quit()

    def test_add_driver_license_personal_camping_option(self):
        driver = webdriver.Chrome()
        driver.get('https://cnt-784b233b-3492-4228-8423-83e3047817c1.containerhub.tripleten-services.com')

        # Crie uma instância da classe de página
        urban_routes_page = UrbanRoutesPage(driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        driver.implicitly_wait(3)

       # Escolha a etapa do carro de camping para inserir "De", "Para" e clicar em "personal_option",
        # "carsharing_icon", "book_button", e "camping"
        ...

        # Adicionar a etapa de carteira de motorista para clicar em "adding_driver_license";
        # para inserir "first_name", "last_name", "date_of_birth", "number"; e
        # para clicar em "title" e "add_button"
        ...

        # Verifique se a licença foi adicionada
        actual_value = urban_routes_page.get_verification_text()
        expected_value = "Obrigado!"
        assert expected_value in actual_value, f"Esperado '{expected_value}', mas recebeu '{actual_value}'"
        driver.quit()
