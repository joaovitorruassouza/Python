# ==========================================================================

# Desenvolvedor por: João Vitor Santos

# Desenvolvido na data 09/04/19

# E-mail: joaovitorruassouza@hotmail.com

# ==========================================================================

print('Olá, bem-vindo ao painel do administrador ')

print('Faça o Login para continuar.')
#===============================================
# Variáveis para teste
#===============================================

exit1 = 'Usuário ou Senha inválidos!'
exit0 = 'Login feito com sucesso!'


# Variáveis para o Login

username = str(input('USUÁRIO: '))
password = str(input('SENHA: '))


# Idêntificar se é letra, (alfabeto)

typeprimitive = (username.isalpha())

# Condições sobre condições

if typeprimitive == 0:
    print('Erro, não aceitamos valores númerais ou com simbolos !\nTente novamente...')

elif typeprimitive == 1:

    if username == 'joaovitorruas':
        if password == 'qwe123':
            print(f'Saída de status (0)\n{exit0}')
            print('O que deseja acessar ?')
            print('=-' * 5)
            print('Login do Hotmail (1)')
            print('Login do Gmail (2)')
            print('Login do League of legends (3)')
            terminal = input('$: ')
            terminal_value = terminal.isnumeric()
            if terminal_value == 1:
                if terminal == '1':
                    print('Ok, você quis acessar os seus dados do Hotmail:')
                    print('Usuário: (Morango_SemDente@mail.com)')
                    print('Senha: (manga123')
                    print(' ')
                    print('Usuário: (pyhonfundamentos2019@hotmail.com')
                    print('Senha: (testeemail00)')

                elif terminal == '2':
                    print('Ok, você quis acessar os seus dados do Gmail')
                    print('Usuário: (Pera_Salgada@mail.com)')
                    print('Senha: (abobora123)')
                    print(' ')
                    print('Usuário: (salgado_azedo@mail.com)')
                    print('Senha: (sabao123)')

                elif terminal == '3':
                    print('Ok, você quis acessar os seus dados do League of Legends')
                    print('Usuário: (teste123)')
                    print('Senha:(senha321)')
                    print(' ')
                    print('Usuário: (barrigade7almoco')
                    print('Senha: (torta0130)')

            elif terminal_value == 0:
                print('Aceitamos somente números!')

            else:
                print('Erro incomum encontrado... contate o desenvolvedor')

        elif password != 'qwe123':
            print(f'Códico do erro (1)\n{exit1}')

    elif username != 'joaovitorruas':
        print('Códico do erro (1)\nUsuário ou Senha inválidos!')

else:
    print('Erro não conhecido pelo sistema !')


exit(0)
