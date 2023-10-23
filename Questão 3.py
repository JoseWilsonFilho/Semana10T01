valor = 0
for i in range(100):
    numeros = int(input())
    valor = numeros + valor
media = (valor / 100)
print(f'{media:.2f}')