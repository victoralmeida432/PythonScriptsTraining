#Exercício Python 014: 
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input("Digite a Temperatura em graus Celsius: "))
fahrenheit = ((9*temperatura)/5)+32

print("A temperatura de {} Graus Celsius corresponde a {} Graus Fahrenheit".format(temperatura,fahrenheit))
