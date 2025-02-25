import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM


def test_personal_bike_option():
    driver = webdriver.Chrome()
    # Etapa 1: Abra o aplicativo e atualize a URL após iniciar o servidor
    driver.get('https://cnt-fd677479-89ab-4ea3-ad09-0999796f6ec8.containerhub.tripleten-services.com')

   # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)

    # Etapa 2: use métodos POM para executar ações na página
    # Insira os locais "De" e "Para".
    ...

    # Selecione a opção "Personal".
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Clique no ícone "Bicicleta".
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 3: Verifique se o texto da bicicleta é exibido corretamente
    actual_value = ...
    expected_value = ...
    assert ...
    driver.quit()

