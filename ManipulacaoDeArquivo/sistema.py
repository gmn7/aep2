
menu=0
while menu !=3:
    n=0
    print ('''    [1] Adicionar lista de compra
    [2] Visualizar Lista
    [3] Sair do programa
    ''')
    menu = int(input("informe uma opcão: "))
    if menu == 1:
        while n != 2:
           n = int (input('''Selecione:  [1]Para Adicionar Produto 
           [2]Para voltar para o menu
           : '''))
           if n == 1:
                 produto = input ("informe o produto a adicionar a lista: ")
                 arquivo = open('teste.txt', 'a')
                 arquivo.write(produto)
                 arquivo.close()
                 print ("Dados inseridos com Sucesso")
    elif menu == 2:
         while n != 2:
             n = int(input('''Selecione    [1] Para mostrar a lista de compra 
             [2] Para voltar para o Menu: 
             : '''))
             if n == 1:
                arquivo = open('teste.txt', 'r')
                conteudo = arquivo.read()
                print(conteudo)
    else:
        print ("opção invalida")
print("fim do programa")