# Exercício Python 039: 
# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar 
# ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input("Digite o ano de nascimento: "))
idade = atual - nasc
print("Quem nasce em {} tem {} anos em {}".format(nasc,idade,atual))
if idade == 18:
    print("Você precisa se alistar")
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18: 
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))


