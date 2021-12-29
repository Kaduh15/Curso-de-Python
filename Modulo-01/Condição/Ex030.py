"""Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

num = int(input('Digite um valor: '))

if num % 2 == 0:
    print(f'O número {num} é PAR!!')
else:
    print(f'O número {num} é IMPAR!!!')
