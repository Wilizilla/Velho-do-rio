#print (123)
# print (456)
# int('a') retorna um erro
var_num = input('Vou dobrar o numero que você digitar: ')

if var_num.isdigit():
    var_num_float = float(var_num)
    print (f'O dobro de {var_num_float} é {var_num_float * 2}')

else:
    print('Isso não é um número')