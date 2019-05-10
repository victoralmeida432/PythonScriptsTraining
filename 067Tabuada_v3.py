# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo. 
table = 0
while True:
    num = int(input("Digite um número para saber sua tabuada: "))
    if num < 0:
        break
    else:
        for c in range(1,11):
            table = num * c
            print("{} x {} = {}".format(num,c,table))
print('FIM')
