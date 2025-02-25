import time
from selenium import webdriver

from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM


def test_add_driver_license_personal_camping_option():
    driver = webdriver.Chrome()
    # Abra o aplicativo e atualize a URL após iniciar o servidor
    driver.get('https://cnt-932267f3-a263-441e-ac4d-b70fa84058e0.containerhub.tripleten-services.com')

    # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)

    # Etapa 1: Insira o endereço "De"
    ...

    # Etapa 2: Insira o endereço "Para"
    ...

    # Etapa 3: Escolha "Personal"
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 4: Clique em "Carsharing"
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 5: Clique em "Reservar"
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 6: Escolha "Camping"
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 7: Clique em “Adicionar uma carteira de motorista”
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 8: Preencha o campo “Nome”
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 9: Preencha o campo “Sobrenome”
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 10: Preencha o campo “Data de nascimento”
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 11: Preencha o campo “Número”
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 12: Clique em "título" para tornar clicável o botão Adicionar
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 13: Clique em “Adicionar”
    ...
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 14: Verifique se a licença foi adicionada
    actual_value = ...
    expected_value = ...
    assert ...
    driver.quit()


