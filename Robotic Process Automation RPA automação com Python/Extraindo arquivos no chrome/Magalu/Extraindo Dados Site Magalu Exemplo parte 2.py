from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pyautogui as funcoesTeclado

navegador = opcoesSelenium.Chrome()

# Abre o navegador e acessa o site do Magazine Luiza
navegador.get("https://www.magazineluiza.com.br/")

tempoEspera.sleep(1)

# Procura o campo de busca e insere o texto celulares
navegador.find_element(By.XPATH, '//*[@id="input-search"]').send_keys('celulares')

tempoEspera.sleep(1)

# Aperta a tecla enter para realizar a busca
funcoesTeclado.press('enter')

tempoEspera.sleep(3)

listaProdutos = navegador.find_elements(By.CLASS_NAME, "iTkWie")

# Adiciona um loop para percorrer todos os produtos encontrados
for item in listaProdutos:
    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""
    
    # Tenta encontrar o nome do produto usando duas classes diferentes
    try:
        nomeProduto = item.find_element(By.CLASS_NAME, "iWaBVz").text
    except Exception:
        pass
    
    if nomeProduto == "":
        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "sc-gQSkpc").text
        except Exception:
            pass  
    # Verifica se o nome do produto foi encontrado antes de imprimir
    if nomeProduto:
        print(nomeProduto)
        
#------------------------------------------------------------
    if precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-dcJsrY").text
        except Exception:
            pass
    if precoProduto:
        print(precoProduto)

    if urlProduto == "":
        try:
            urlProduto = item.find_element(By.CLASS_NAME, "sc-dcJsrY").text
        except Exception:
            pass
    if urlProduto:
        print(urlProduto)