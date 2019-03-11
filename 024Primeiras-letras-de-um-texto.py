#Exercício Python 024: Crie um programa 
# que leia o nome de uma 
# cidade diga se ela começa ou não com o nome "SANTO"

cidade = str(input("Digite o nome da sua cidade: ")).upper().strip()
print(cidade[:5] == 'SANTO')