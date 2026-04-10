idade = 20

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))



print()

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if not login:
    print("Ow... seja mais inteligente! Loga ai...")




print()

nota_final = 6

if nota_final < 4:
    print("Reprovado")

elif nota_final < 6:
    print("Recuperação")

else:
    print("Aprovado")

print("FIM")
