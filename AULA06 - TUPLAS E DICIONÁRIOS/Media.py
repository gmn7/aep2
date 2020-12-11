#Construa um algoritmo que peça ao usuário para informar o nome, 
# a nota01 e a nota02 de um aluno. Guarde estas informações em um dicionário. 
# Após, calcule a nota final deste aluno [(nota01 + nota02) /2] e adicione ao dicionário. Ao final,
# imprima todos os dados do dicionário.

aluno = dict ()
aluno ['nome'] = str(input('Nome: '))
nota1 = float(input("Informe a primeira nota: "))
aluno ['nota1'] = nota1
nota2 = float(input("informe a segunda"))
aluno['nota2'] = nota2
media = [(nota1 + nota2)/2]
aluno['media'] = media
print(aluno)
