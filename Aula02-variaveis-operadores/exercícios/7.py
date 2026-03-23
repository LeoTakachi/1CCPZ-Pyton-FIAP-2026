""" Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que
o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor
unitário de cada peça2. Após, calcule e mostre o valor a ser pago. """

peca1 = input("Digite o nome da primeira peça: ")
quant1 = int(input("Digite a quantidade da primeira peça: "))
valor1 = float(input("Digite o valor unitário da primeira peça: "))

peca2 = input("Digite o nome da segunda peça: ")
quant2 = int(input("Digite a quantidade da segunda peça: "))
valor2 = float(input("Digite o valor unitário da segunda peça: "))

total = (quant1 * valor1) + (quant2 * valor2)

print(f"Valor total a pagar: R$ {total:.2f}")
