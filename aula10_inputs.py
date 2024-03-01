var_name = input('Qual seu nome? ')
 
#Para salvar o input é necessário colocalo dentro de uma variável
var_number01 = input ('Digite um número: ')
var_number02 = input ('Digite um número: ')
var_convert01 = float(var_number01)
var_convert02 = float(var_number02)
# para transformar o input em um número é necessário converter a váriavel que armazenou o input
# o ideal é converter em uma nova variável para evitar falhas ao tenar converter texto para float ou int

print()
print(f'{var_name}, a soma dos números é {var_convert01 + var_convert02 :.2f}')