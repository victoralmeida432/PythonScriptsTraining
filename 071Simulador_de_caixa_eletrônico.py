# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar 
# quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=-="*20)
print("Caixa Eletronico")
print("=-="*20)
valor = int(input("Digite o valor do saque: "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print("Total de {} cédulas de R${}".format(totced,ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("=-="*20)
print("Volte sempre e tenha um ótimo dia.")
    
    
'''


# # -*- coding: utf-8 -*-

valor = int(input(""))
total = valor
ced = 100
totced = 0
print(valor)
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced >= 0:
            print("{} nota(s) de R$ {},00".format(totced,ced))
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        elif ced == 1:
            ced = 0
        totced = 0
        if total == 0:
            # print("{} nota(s) de R$ {},00".format(totced,ced))
            break
            
 
    
