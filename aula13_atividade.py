var01 = input('Digite o primeiro valor ')
var02 = input('Digite o segundo valor ')

text01 = ('primeiro número')
text02 = ('segundo número')

if var01 > var02:
    par01 = text01
    par02 = text02
    result = f'O {par01} é maior que o {par02}'

elif var02 > var01:
    par01 = text02
    par02 = text01
    result = f'O {par01} é maior que o {par02}'

else:
    result = f'Os números são iguais'

print (result) 