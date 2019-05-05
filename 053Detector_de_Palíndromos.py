#Exercício Python 053: 
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços.

frase = str(input("Digite uma frase para checar se ela é um palindromo: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1]
#Elimina o for e a lista INVERSO que está vazia e tá safe

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

print("A Frase digitada foi: {}".format(frase))
print("E seu inverso é: {}".format(inverso))
if inverso == junto:
    print("A frase é um palindromo.")
else:
    print("A frase NÃO é um palindromo.")
