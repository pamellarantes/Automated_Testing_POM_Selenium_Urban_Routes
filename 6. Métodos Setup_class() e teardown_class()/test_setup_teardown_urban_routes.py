from selenium import webdriver
import time
from urban_routes_main_page import UrbanRoutesPage

# Crie uma classe para ambos os testes
class TestUrbanRoutes:

    # Inicialize o driver do Chrome uma vez para a classe
    @classmethod
    def setup_class(cls):
        ...

    def test_personal_bike_option(self):
        self.driver.get('https://cnt-8f25f166-edc1-4f8d-b177-7e4079036890.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(self.driver)
        ...
        assert ...

    def test_duration_personal_bike_option(self):
        self.driver.get('https://cnt-8f25f166-edc1-4f8d-b177-7e4079036890.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(self.driver)
        ...
        assert ...

    # Feche o navegador depois que todos os testes forem feitos
    @classmethod
    def teardown_class(cls):
        ...