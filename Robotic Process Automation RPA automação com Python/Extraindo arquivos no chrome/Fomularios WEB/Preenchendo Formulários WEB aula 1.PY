from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()
navegador.get("https://form.jotform.com/221436066464051")

#Tempo para o computador processar as informações
tempoEspera.sleep(4)

#Preenchendo o campo de texto com o nome
navegador.find_element(By.NAME, "q3_nome[first]").send_keys("Joao Pedro")

#Tempo para o computador processar as informações
tempoEspera.sleep(1)

#Preenchendo o campo de texto com o sobrenome
navegador.find_element(By.NAME, "q3_nome[last]").send_keys("de Souza")

#Tempo para o computador processar as informações
tempoEspera.sleep(1)

#Preenchendo o campo de texto com o email
navegador.find_element(By.NAME, "q4_email").send_keys("joao@hotmail.com")

#Tempo para o computador processar as informações
tempoEspera.sleep(3)

pegaDropDraw = navegador.find_element(By.ID, "input_5")
itemSelecionado = Select(pegaDropDraw)
itemSelecionado.select_by_index(2)

#Tempo para o computador processar as informações
tempoEspera.sleep(2)

filho = "Não"

if filho == "Sim":
    # Marca a opção tem filhos / Sim
    navegador.find_element(By.ID, "label_input_6_0").click()
else:
    # Marca a opção tem filhos / Não
    navegador.find_element(By.ID, "label_input_6_1").click()
    
#Tempo para o computador processar as informações
tempoEspera.sleep(2)

# Marca a opção de cor favorita
navegador.find_element(By.ID, "label_input_7_4").click()

#Tempo para o computador processar as informações
tempoEspera.sleep(2)

navegador.find_element(By.ID, "label_input_7_2").click()

#Tempo para o computador processar as informações
tempoEspera.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[3]').click()

#Tempo para o computador processar as informações
tempoEspera.sleep(2)