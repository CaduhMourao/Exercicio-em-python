valor = float(input('Valor do produto: '))
soma = valor * 5
desconto = soma / 100
valorFinal = valor - desconto

print(f'O valor do produto de R${valor} fica R${valorFinal} com desconto.')