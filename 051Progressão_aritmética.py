# Exercício Python 051: Desenvolva um programa que leia o primeiro 
# termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro,decimo,razao):
    print('{}'.format(c),end =' -> ')
print('Acabou.')