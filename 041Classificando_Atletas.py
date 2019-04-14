# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Confederação Nacional de Natação")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

atual = date.today().year
nasc = int(input("Digite o ano de nascimento: "))
idade = atual - nasc

if idade <= 9:
    print("Você tem {} anos, você é da catégoria: MIRIM".format(idade))

elif idade <= 14:
    print("Você tem {} anos, você é da catégoria: INFANTIL".format(idade))

elif idade <= 19:
    print("Você tem {} anos, você é da catégoria: JÚNIOR".format(idade))

elif idade <= 25:
    print("Você tem {} anos, você é da catégoria: SÊNIOR".format(idade))

elif idade > 25:
    print("Você tem {} anos, você é da catégoria: MASTER".format(idade))

