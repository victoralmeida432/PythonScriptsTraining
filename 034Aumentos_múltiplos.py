#Exercício Python 034: Escreva um programa que pergunte o 
# salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o seu salário: "))
if salario > 1250:
    aumento = (1250 * 10) / 100
    novo_salario = salario + aumento
    #print(aumento)
    print("Seu novo salário é de R${}".format(novo_salario))
else:
    aumento2 = (1250 * 15) / 100
    novo_salario2 = salario + aumento2
    #print(aumento2)
    print("Seu novo salário é de R${}".format(novo_salario2))