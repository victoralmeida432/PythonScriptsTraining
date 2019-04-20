# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
#  considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o valor do produto: "))
opcao = int(input(""" Digite a opção de pagamento:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão (Debito): 5% de desconto
[3] Em até 2x no cartão de crédito: Preço sem alterações
[4] 3x ou mais no cartão de crédito: 20% de juros
Escolha: """))

if opcao == 1:
    desconto = (preco * 10) / 100
    novo_valor = preco - desconto
    print("O preço que era de R${:.2f} com desconto de R${:.2f} ficará: R${:.2f}".format(preco,desconto,novo_valor))

elif opcao == 2:
    desconto = (preco * 5) / 100
    novo_valor = preco - desconto
    print("O preço que era de R${:.2f} com desconto de R${:.2f} ficará: R${:.2f}".format(preco,desconto,novo_valor))

elif opcao == 3:
    qtd_parcelas = int(input("Em quantas vezes você deseja parcelar? (Máximo 2x)"))
    if qtd_parcelas >= 3:
        print("Nessa opção a quantidade máxima de vezes que você pode parcelar é 2x.")
    else:
        parcelas = preco / qtd_parcelas
        print("O valor de R${:.2f} dividido em {} vezes dará em {} parcelas de R${:.2f}".format(preco,qtd_parcelas,qtd_parcelas,parcelas))

elif opcao == 4:
    qtd_parcelas = int(input("Em quantas vezes você desejar parcelar? (Minimo de 3x) "))
    if qtd_parcelas < 3:
        print("You burro man?!")
    else:
        juros = (preco * 20) / 100
        novo_valor = preco + juros
        parcelas = novo_valor / qtd_parcelas
        print("O preço que era {:.2f} ficará {:.2f} com o juros de 20%, dividido em {} parcelas de R${}".format(preco,novo_valor,qtd_parcelas,parcelas))
