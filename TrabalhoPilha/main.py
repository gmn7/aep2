from pilha import Pilha

def menu():
    print ('Entre com a opcao: \n', \
            '1 para inserir na pilha \n', \
            '2 para retirar na pilha\n', \
            '3 para mostra o proximo valor a ser retirado da pilha \n', \
            '4 verificar se esta vazia \n', \
            '5 para finalizar o programa \n')

pilha = Pilha()
menu()
contro = input("informe uma opcao: ")

while contro !=5:
    if contro =='1':
        pilha.push(input('Qual o valor ?'))
    elif contro =='2':
        pilha.pop()
    elif contro =='3':
        pilha.peek()
    elif contro =='4':
        pilha.empty()
        break
    else:
        print ('Opcao invalida', contro)
        menu()
    contro=input('\n')
print ('Programa finalizado')