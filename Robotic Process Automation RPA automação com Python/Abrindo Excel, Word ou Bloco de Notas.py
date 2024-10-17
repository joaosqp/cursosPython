import pyautogui as escolha_opcao

opcao = escolha_opcao.confirm( 
    text ='Escolha uma opção',
    title ='Escolha uma opção', 
    buttons =['Excel', 'Word', 'Bloco de Notas'])

if opcao == "Excel":
    
    print("Você escolheu a opção Excel")
    
elif opcao == "Word":
    
    print("Você escolheu a opção Word")
    
else:
    
    print("Você escolheu a opção Bloco de Notas")