#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maiores_de_idade = 0
menores_de_idade = 0
idade_maiores = []
idade_menores = []
maiores = []
menores = []
for i in range(1,8):
    anonasc = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(i)))
    anoatual = date.today().year
    idade = anoatual - anonasc
    if idade > 150:
        print("Acho que você errou")
        break
    else:
        if idade >= 18:
            maiores += [i]
            idade_maiores += [idade]
            maiores_de_idade += 1
            menores_de_idade += 0
        else:
            menores += [i]
            idade_menores += [idade] 
            menores_de_idade += 1
            maiores_de_idade += 0

print("Essa lista contem {} pessoas maiores de idade".format(maiores_de_idade))
print("E contém {} pessoas menores de idade".format(menores_de_idade))
print("idade dos maiores: {} ".format(idade_maiores))
print("idade dos menores: {}".format(idade_menores))
print("Os maiores de idade são: {}".format(maiores))
print("Os menores de idade são: {}".format(menores))