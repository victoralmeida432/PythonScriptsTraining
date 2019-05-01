# Exercício Python 050: Desenvolva um programa que 
# leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

count = 0
soma = 0
for i in range(1,7):
    num = int(input("Digite {} número: ".format(i)))
    if num % 2 == 0:
        count += 1
        soma += num
print("Foram somados {} números pares".format(count))
print("A soma desses números é {}".format(soma))
