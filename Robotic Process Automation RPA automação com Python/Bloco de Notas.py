import pyautogui as posicaoAbreArquivos
 
#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)
 
#Mesma coisa que pressionar as teclas do teclado
#Windows + R
posicaoAbreArquivos.hotkey('win','r')
 
#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)
 
#Digitando notepad na caixa de executar para
#abrir o bloco de notas
posicaoAbreArquivos.typewrite('notepad')
 
#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)
 
#Apertar a tecla enter para abrir o bloco de notas
posicaoAbreArquivos.press('enter')
 
#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)
 
# Digita o texto com um pequeno atraso entre cada caractere
posicaoAbreArquivos.write('Abri o bloco de notas com o Python', interval=0.25)
 
 
#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)
 
#Permite pegar a janela que está ativa
fecharBlocoDeNotas = posicaoAbreArquivos.getActiveWindow()
 
#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)
 
#Aciona a opção para fechar a janela ativa
fecharBlocoDeNotas.close()
 
#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)
 
#Pressionando a tecla tab para ir para o botão não salvar
posicaoAbreArquivos.press('tab')
 
#Aguarda um tempo para o computador processar informações
posicaoAbreArquivos.sleep(2)
 
#Apertamos a tecla enter para fechar sem salvar
posicaoAbreArquivos.press('enter')
 
print("Automação executada com sucesso!")   
