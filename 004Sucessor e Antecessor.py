#Python Exercise 005: 
# Make a program that reads an integer and show on the screen
# its successor and predecessor.

num = int(input("Digite um número inteiro para saber seu sucessor e antecedor: "))
sucessor = num + 1
antecessor = num - 1
print("O sucessor de {} é {}".format(num,sucessor))
print("O antecessor de {} é {}".format(num,antecessor))