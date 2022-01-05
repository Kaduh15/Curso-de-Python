"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. """

num = int(input('Digite um número inteiro: '))
opcao = int(input('''
1) Binário
2) Octal
3) Hexadecimal
Para que opção deseja converter: '''))

if opcao == 1:
    print(f'O número {num} em Binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} em Octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} em Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção errada! FIM DO PROGRAMA')
