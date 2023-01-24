valor = float(input('Valor do produto: '))
desconto = valor - (valor * 5 / 100)

print(f'O valor do produto de R${valor:.0f} fica R${desconto:.0f} com desconto.')