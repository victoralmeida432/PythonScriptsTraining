# Exercício Python 048: Faça um programa que calcule a soma entre todos os 
# números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

count = 0
soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        #soma += c
        soma = soma + c
        #count = count + 1
        count += 1
print('Foram somados {} valores'.format(count))
print('A soma de todos os valores solicitados é {}'.format(soma))