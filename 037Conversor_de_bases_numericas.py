# Exercício Python 037: Escreva um programa em Python que leia um número inteiro 
# qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))
escolha = int(input("""
Escolha uma dessas bases para conversão:
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
Sua opção: 
"""))

if escolha == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num,bin(num)))

elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)))

elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)))
else:
    print("Opção invalida, por favor, digite uma opção válida.")