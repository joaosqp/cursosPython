from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pandas as pd

# Inicializando o navegador
navegador = opcoesSelenium.Chrome()

# Abrindo o site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

# Localizando a tabela na página
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")

# Extraindo os dados das linhas da tabela
dataFrame = []
for linhaAtual in linhas:
    print(linhaAtual.text)
    dataFrame.append([linhaAtual.text])  # Lista de listas para compatibilidade com DataFrame

# Criando um DataFrame do pandas
df = pd.DataFrame(dataFrame, columns=['Dados'])

# Preparando para salvar no Excel usando xlsxwriter
arquivoExcel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')

# Salvando o DataFrame no arquivo Excel
df.to_excel(arquivoExcel, sheet_name='Sheet1', index=False)

# Fechando o ExcelWriter para garantir a gravação correta
arquivoExcel.close()
