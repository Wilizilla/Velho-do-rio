name = 'Wilian Siqueira'
height = 1.74
weight = 99
imc = weight /(height ** 2)

print(name, 'tem', height, 'M de altura' )
print('Pesa', weight, 'quilos e seu imc é:')
print(imc)

print()

line_01= f'{name} tem {height:.2f}M de altura'
line_02= f'Pesa {weight} quilos e seu imc é:'
line_03= f'{imc:.2f}'

print(line_01)
print(line_02)
print(line_03)