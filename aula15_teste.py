#teste git 4
var_name = input('Digite o seu nome: ')
var_age = input('Digite a sua idade: ')
if var_name and var_age :
    print()
    print('Seu nome é:',var_name)
    print('Seu nome de trás para frente é:', var_name[::-1])
    print()
    print('Seu nome tem', len(var_name), 'letras',)
    print('Sua idade é:', var_age, 'anos')
    print()

    if ' ' in var_name:
        print('Seu nome CONTÉM espaços')

    else: 
        print('Seu nome NÃO contém espaços')
        
    print()
    print('A primeira letra do seu nome é:', var_name[0])
    print('A última letra do seu nome é:', var_name[-1])

#elif var_name != '' and var_age == '':
#    print('Seu nome é:',var_name)

#elif var_name == '' and var_age != '':
#    print('Sua idade é:',var_age)

else: 
    print('Dados incompletos.')
