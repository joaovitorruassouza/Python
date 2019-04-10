# ==========================================================================

# Desenvolvedor por: João Vitor Santos

# Desenvolvido na data 09/04/19

# E-mail: joaovitorruassouza@hotmail.com

# ==========================================================================

# Desafio: Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# Apresentação, Desafio Web

# Conseguir fazer o programa funcionar dessa mandeira

# ===========================================================================

print('=== Desafio 004 ===')

print('========== SISTEMA DE NOTAS ==========')

#===============================================================
# Variável value1 recebe o valor de input continuo em value2,3,4
#===============================================================

value1 = input('Digite a primeira nota: ')
#==============================================================================================
# Verificar se é um número, v1 recebe a informação de .isnumeric() confirmando em true ou false
#==============================================================================================

v1 = (value1.isnumeric())

### CONDIÇÕES ###

# Se a variável v1 for igual a 1 (True) se repete em todos as condições, em todas as condições

if v1 == 1:
    value2 = input('Digite a segunda nota: ')
    v2 = (value2.isnumeric())
    if v2 == 1:
        value3 = input('Digite a terceira nota: ')
        v3 = (value3.isnumeric())
        if v3 == 1:
            value4 = input('Digite a quarta nota: ')
            v4 = (value4.isnumeric())
            if v4 == 1:
                print('=-'*20)
                print(f'Primeira nota: {value1}\nSegunda nota: {value2}\nTerceira nota: {value3}\nQuarta nota: {value4}')
                print('=-*20')
                soma = int(value1) + int(value2) + int(value3) + int(value4)
                media = soma / 4
                print('=-'*20)
                print('Resultado: ')

                if media > 100:
                    print('A nota de aluno não vai além de 100, colocou a nota de maneira correta ?')
                    print('=-'*20)

                elif media >= 6:
                    print(f'Aluno Aprovado!\nA média foi: {media}')
                    print('=-'*20)

                elif media < 6:
                    print(f'Aluno Reprovado!\nA média foi: {media}')
                    print('=-'*20)

                else:
                    print('Erro desconhecido...')

            else:
                print('Eu só aceito números')

        else:
            print('Eu só aceito números')

    else:
        print('Eu só aceito números')

else:
    print('Aceito somente números inteiros!')

exit(0)
