from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pyautogui as funcoesTeclado
import pandas as pd

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

# Cria uma lista vazia para armazenar os dados
listaDataFrame = []

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

        
# Precisa encontrar o preço do produto usando várias classes diferentes
    if precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-dcJsrY").text
        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "eLxcFM").text
        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-eHsDsR").text
        except Exception:
            pass        
    elif precoProduto == "":
        try:
            precoProduto = item.find_element(By.CLASS_NAME, "eGPZvr").text
        except Exception:
            pass            
        
# precisa encontrar a URL do produto usando várias classes diferentes
    if urlProduto == "":
        try:
            urlProduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            pass
    else:
        print("Não foi possível encontrar a URL do produto")
        
    print(nomeProduto ,"-", precoProduto)
    print(urlProduto)
    
    dadosLinha = nomeProduto + ";" + precoProduto + ";" + urlProduto
    
    # Adiciona os dados da linha à lista
    listaDataFrame.append(dadosLinha)
    
arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
arquivoExcel.close()

df = pd.DataFrame(listaDataFrame, columns=['Descrição ; Preço; URL'])

arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')

df.to_excel(arquivoExcel, sheet_name='Dados', index=False)

arquivoExcel.close()