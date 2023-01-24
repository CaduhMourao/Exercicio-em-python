# n = float(input('Entre com um valor: '))
# d = n * 2
# t = n * 3
# r = n ** (1/2)

# print(f'O dobro de {n} é {d} e o triplo é {t} e a raiz quadrada é {r:.2f}.')

# corrigindo

n = int(input('Digite um número: '))
print(f'O dobro de {n} é {n*2}, o triplo de {n} é {n*3} e a raiz quadrada é {pow(n, (1/2)):.2f}')