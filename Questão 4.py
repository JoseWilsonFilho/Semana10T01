sequencia = ''
for i in range(10 , 1010, 10):
    sequencia += str(i) + ',' + ' '  
sequencia = sequencia.strip()
sequencia = sequencia[:-1]
print(f'{sequencia}.')