#Exercício Python 022: Crie um programa que leia o nome 
# completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas;
#– Quantas letras ao todo (sem considerar espaços);
#– Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome: ")).strip()
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
tamanho_nome = len(nome)-nome.count(' ')
primeiro_nome = nome.split()
nletras_1nome = len(primeiro_nome[0])

print("Analisando seu nome...")
print("Seu nome em maisculas é {}".format(nome_maiusculo))
print("Seu nome em minusculas é {}".format(nome_minusculo))
print("Seu nome tem ao todo {} letras".format(tamanho_nome))
print("Seu primeiro nome é {} e ele tem {} letras".format(primeiro_nome[0],nletras_1nome))