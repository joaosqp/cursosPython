import pyautogui as posiçãoMouse
import pyautogui as tempoEspera

# Movendo até o botão iniciar
posiçãoMouse.moveTo(x=625, y=1058)

# Tempo de espera para o mouse se mover
tempoEspera.sleep(3)

# Clicando no botão iniciar
posiçãoMouse.click(x=625, y=1058)

# Tempo de espera para o mouse se mover
tempoEspera.sleep(3)

# Escrevendo a palavra Google Chrome
posiçãoMouse.typewrite('Google Chrome')

# Tempo de espera para pressionar a tecla enter
tempoEspera.sleep(3)

# Pressionando a tecla enter
posiçãoMouse.press('enter')

# Tempo de espera para o mouse se mover
tempoEspera.sleep(2)

# Escrevendo a palavra Cotação do Dólar hoje
posiçãoMouse.typewrite('Cotacao do Dolar hoje')  

# Tempo de espera para pressionar a tecla enter
tempoEspera.sleep(2)

# Pressionando a tecla enter
posiçãoMouse.press('enter')   