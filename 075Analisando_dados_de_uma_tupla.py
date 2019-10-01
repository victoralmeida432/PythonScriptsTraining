# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))

tupla = (valor1,valor2,valor3,valor4)

print("sua tupla foi: {} ".format(tupla))
if 3 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes')
else:
    print("O valor 3 não foi digitado em nenhuma posicão.")
print(f'A primeira vez que o número 3 apareceu foi {tupla.index(3)+1} posição')
print("Os valores pares digitados foram: ",end =' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end=', ')
