"""Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint

pc = randint(0, 5)

num = int(input("""Olá, eu pensei em número entre 0 e 5. consegue adivinhar?
Qual número eu pensei? 2
"""))

if num == pc:
    print('Você acertou!!!')
else:
    print('Você perdeu!!!')
