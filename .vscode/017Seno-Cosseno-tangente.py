#Exercício Python 018: Faça um programa que leia um ângulo 
#qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input("Digite o ângulo desejado: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O seno de {} é {:.2f}".format(angulo,seno))
print("O cosseno de {} é {:.2f}".format(angulo,cosseno))
print("O tangente de {} é {:.2f}".format(angulo,tangente))