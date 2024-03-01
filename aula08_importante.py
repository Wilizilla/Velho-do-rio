print()
print('Exemplo 1')
a = 'Wilian'
b = 'Siqueira'
c = 1.74

var_dados = 'Nome:{} Sobrenome:{} Altura:{:.3f}'

#formato = 'Nome:{} Sobrenome:{} Altura:{} não existe{}' 
# causaria um erro pq não existem 4 parametros

var_imprimir = var_dados.format(a, b, c) #format é um MÉTODO e "a" são argumentos

print(var_imprimir)

#--------------------------------------------------------
print()
print('Exemplo 2')

d = 'Wilian'
e = 'Siqueira'
f = 1.74

var_dados02 = 'Nome:{0} Sobrenome:{0} Altura:{2:.3f}'
# exemplo do uso de indices
var_imprimir02 = var_dados02.format(d, e, f)

print(var_imprimir02)

#--------------------------------------------------------
print()
print('Exemplo 3')

g = 'Wilian'
h = 'Siqueira'
i = 1.74

var_dados03 = 'Nome:{first_name} Sobrenome:{second_name} Altura:{height03:.3f}'
# exemplo do uso de parametros exemplo parametro=argumento
var_imprimir03 = var_dados03.format(
    first_name=g, second_name=h, height03=i
)

print(var_imprimir03)