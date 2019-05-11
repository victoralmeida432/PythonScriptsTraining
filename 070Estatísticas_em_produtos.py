# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

print("=-="*20)
print("Lista de compras!")
print("=-="*20)

total = 0
totmil = 0
cont = 0
menor = 0
barato = ''
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print('O total da compra foi {} Reais'.format(total))
print("Temos {} produto(s) que custa(m) mais de 1000 reais.".format(totmil))
print("O menor preço custa {} reais".format(menor))
print("O nome do produto mais barato foi: {}".format(barato))                         

