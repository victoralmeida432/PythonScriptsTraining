#Exercício Python 017: 
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjecente: "))
hip = (co**2 + ca**2) ** (1/2)

print("A hipotenusa vai medir {:.2f}".format(hip))