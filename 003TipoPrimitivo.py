#Exercício Python 004: 
# Faça um programa que leia algo pelo teclado e mostre 
# na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

frase = str(input("Digite alguma coisa: "))
print("O tipo primitivo desse valor é: ",type(frase))
print("Só tem espaço?", frase.isspace())
print("é um número",frase.isnumeric())
print("é alfabético",frase.isalpha())
print("é alfanúmerico?",frase.isalnum())
print("Está em maisculas?",frase.isupper())
print("Está em minusculas?",frase.islower())
print("está capitalizada?",frase.istitle())