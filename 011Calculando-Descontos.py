#Exercício Python 012: 
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto.

preco = float(input("Digite o preço do produto: "))
desconto = (preco * 5) / 100
novo_preco = preco - desconto
print("O produto que custava {} passará a custar".format(preco))
print("{} com desconto de 5%.".format(novo_preco))