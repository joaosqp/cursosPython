from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

#Tempo para o computador processar as informações
tempoEspera.sleep(4)

#Inserindo um CEP na caixa de CEP do busca CEP
navegador.find_element(By.NAME, "endereco").send_keys("05892387")

#Tempo para o computador processar as informações
tempoEspera.sleep(2)

#Clica no botão de Pesquisar
navegador.find_element(By.NAME, "btn_pesquisar").click()

#Tempo para o computador processar as informações
tempoEspera.sleep(4)

#Pega os dados da rua no site pelo XPATH
rua = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
print("Rua:", rua)

#Pega os dados do bairro no site pelo XPATH
bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
print("Bairro:", bairro)

#Pega os dados da cidade no site pelo XPATH
cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
print("Cidade:", cidade)

#Pega os dados do cep no site pelo XPATH
cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
print("CEP:", cep)
