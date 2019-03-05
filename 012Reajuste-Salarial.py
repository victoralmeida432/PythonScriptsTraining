#Exercício Python 013: 
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual o Salario do funcionario? R$"))
aumento = (salario * 15) / 100
novo_salario = salario + aumento

print("Um funcionario que ganhava R$ {}, com 15% de aumento, passa a receber R${:.2f}".format(salario,novo_salario))
