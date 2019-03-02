# Exercício Python 008: 
# Escreva um programa que leia um valor em metros e
#  o exiba convertido em centímetros e milímetros.

valor = float(input("Digite um valor em metros para converte-lo: "))
cm = valor * 100
mm = valor * 1000
print("{}M convertido para centimetros é {} e para milimetros é {}".format(valor,cm,mm))