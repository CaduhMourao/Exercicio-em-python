salario = float(input('Valor do salario: '))
soma = salario * 15
reajuste = soma / 100
reajusteFinal = salario + reajuste

print(f'O valor do salario de R${salario} fica R${reajusteFinal} com reajuste.')