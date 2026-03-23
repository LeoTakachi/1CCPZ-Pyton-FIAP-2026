""" Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.
▪ Exemplo: nota a * 4 e nota b * 6 """

A = float(input("Digite a primeira nota: "))

B = float(input("Digite a segunda nota: "))

MEDIA = (A * 4) + (B * 6) / 4 + 6

print(MEDIA)
