import mysql.connector
connection = mysql.connector.connect(host = 'localhost', user='root', password = '', database = 'mercado')
cursor = connection.cursor(dictionary=True)
class Controller:

    def __init__(self,nome,valor,date):
        self.nome = nome
        self.valor = valor
        self.date = date

    def menu(self):
        print ('''        [1] Adicionar lista de compra
        [2] Remover um item Lista De Compra
        [3] Localizar Lista De Compra
        [4] Sair do programa
        ''')
        return int(input("informe uma opcão: "))

    def adiciona(self):
        n = int (input('''Selecione: [1]Para Adicionar Produto 
           [2]Para voltar para o menu
           : '''))

        if n == 1:
            produto = input("Adicione um produto: ")
            valor = float(input("Adicione um valor: "))
            data =  input("Adicione uma data no padrão Ano-Mês-Dia: ")
            cursor.execute("INSERT INTO produtos(produto, valor, data) VALUES('{}', {}, '{}')".format(produto,valor,data))
            connection.commit()
            print ("Dados inseridos com Sucesso")        
        return n

    def remover(self):
        n = int(input('''Selecione:  [1] Para remover algum intem da lista 
            [2] Para voltar para o Menu: 
            : '''))
        if n == 1:
            produto = input ("Coloque o Nome Do Produto Que Deseja Excluir: ")
            data = input("Informe A Data Ano-Mês-Dia que1 deseja Excluir: ")
            cursor.execute(" DELETE FROM produtos WHERE produto='{}' && data='{}' ".format(produto,data))
            connection.commit()
            print("Dado Apagado com sucesso...")
            print("Aguarde Voltando Ao Menu ...")
        return n
    
    def busca(self):
        n = int(input('''Selecione:  [1] Para Procurar a lista de compra  
            [2] Para Sair
            : '''))
        if n == 1:
            data = input("Selecione a data que deseja buscar pelo ano-mes-dia: ")
            cursor.execute("SELECT * FROM produtos WHERE data='{}'  ".format(data))
            lista = cursor.fetchall()
            print(lista)
            cursor.execute("SELECT SUM(valor) from produtos WHERE data='{}' ".format(data))
            total = cursor.fetchall()
            print("valor total da lista: ")
            print(total)
        return n