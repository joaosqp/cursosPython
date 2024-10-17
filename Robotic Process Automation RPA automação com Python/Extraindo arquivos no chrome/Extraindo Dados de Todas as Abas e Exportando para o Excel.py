from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pandas as pd

# Inicializando o navegador
navegador = opcoesSelenium.Chrome()

# Abrindo o site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

# Localizando a tabela na página
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")

linha = 1
listaDataFrame = []

i = 1

while i < 4:
    # Atualiza a tabela e as linhas em cada iteração
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    
    # Itera sobre as linhas e imprime o conteúdo
    for linhaAtual in linhas:
        print(linhaAtual.text)
        listaDataFrame.append(linhaAtual.text)
        
        linha += 1
    
    i += 1 
    
    # Pausa para garantir que a página processe
    tempoEspera.sleep(2)
    
    # Clica no botão de próxima página
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    
    # Pausa após a navegação
    tempoEspera.sleep(2)

print('Fim da extração de dados')

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')
arquivoExcel.close()

df = pd.DataFrame(listaDataFrame, columns=['Dados'])

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')

df.to_excel(arquivoExcel, sheet_name='Dados', index=False)

arquivoExcel.close()