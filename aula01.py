produtos = ['Cerveja','Agua','Refrigerante']
precos = [10, 2, 5]
quantidade = [100,50,20]


def removerItem():
    print(f'escolha um dos {len(produtos)} produto para remover sendo eles')
    for i, p in enumerate(produtos):
        print(f'{i} --- {p}')
    selecao = int(input("selecione: \n"))

    print(selecao)

    if selecao == 0:
        produtos.remove('Cerveja')
        print("voce escolheu remover cerveja seus produtos são: ")
        print(produtos)
    if selecao == 1:
        produtos.remove('Agua')
        print("voce escolheu remover agua seus produtos são: ")
        print(produtos)
    if selecao ==2:
        produtos.remove('Refrigerante')
        print("voce escolheu remover Refrigerante seus produtos são: ")
        print(produtos)
    else:print("produto não encontrado selecione o produto correto")


print(removerItem())

