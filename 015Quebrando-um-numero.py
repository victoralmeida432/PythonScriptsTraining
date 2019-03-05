#Exercício Python 016: Crie um programa que leia um número Real 
# qualquer pelo teclado e mostre na tela a sua porção Inteira.

#from math import trunc
import math
valor = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porcao inteira e {}".format(valor,math.trunc(valor)))
                                                                         # trunc(valor)

#num = float(input("Digite um valor: "))
#print("O valor digitado foi {} e a sua porcao inteira e {}".format(num,int(num)))
                                                                                  