nota_melhor = 0

for i in range(100):
    nota = int(input())
    if nota > nota_melhor:
        nota_melhor = nota

print(nota_melhor)