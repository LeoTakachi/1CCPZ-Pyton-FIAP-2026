"""  Crie um programa que receba o valor do produto e valor pago.
▪ Calcule o troco a ser pago.
▪ O valor do troco deve ser exibido no terminal. """

ValorProduto = float(input("Qual o valor do produto: "))

ValorPago = float(input("Qual o valor pago: "))

Troco = ValorProduto - ValorPago

print(f" O valor do troco é R${Troco:.2f}")
