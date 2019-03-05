#Exercício Python 015: 
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos Km rodados? "))

pagamento_dias = dias_alugados * 60
pagamento_km = km_rodados * 0.15
pagamento_total = pagamento_dias + pagamento_km

print("O total a pagar e de R${:.2f}".format(pagamento_total))


