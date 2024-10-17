import pyautogui as tempoEspera 
import pyautogui as posiçãoMouse 


# Movendo o mouse até o botão iniciar
posiçãoMouse.moveTo(x=625, y=1058)

# Tempo de espera para o mouse se mover
tempoEspera.sleep(3)

# Clicando no botão iniciar
posiçãoMouse.click(x=625, y=1058)

# Escrevendo a palavra calculadora
posiçãoMouse.typewrite('calculadora')

# Tempo de espera para o mouse se mover
tempoEspera.sleep(3)

posiçãoMouse.click(x=712, y=486)

