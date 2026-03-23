""" Converta uma temperatura de Fahrenheit para Celsius. A fórmula de conversão é: Celsius = (Fahrenheit
- 32) * 5/9 """

fahrenheit = float(input("Digite uma temperatura em fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(f"Temperatura em celsius: {celsius:.2f} °c")