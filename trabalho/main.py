from time import sleep
from controle import Controller

menu = 0
controle = Controller('','','')
while menu !=4:
    n=0
    menu = controle.menu()
    if menu == 1:
        while n != 2:
           n = controle.adiciona()
    elif menu == 2:
         while n != 2:
            n = controle.remover()
    elif menu == 3:
        while n != 2:
            n = controle.busca()
        print("Aguarde Voltando Ao Menu ...")
    elif menu == 4:
        print("Finalizando...")
    else:
        print("Numero invalido por favor digite um numero entre 1 e 4 ...")     
    sleep(2)
print("Fim Do Programa")
