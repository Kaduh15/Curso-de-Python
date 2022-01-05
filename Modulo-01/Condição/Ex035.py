"""Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o Último lado: '))

if ((b - c) < a < b + c) and ((a - c) < b < a + c) and ((a - b) < c < a + b):
    print('É possivel fazer um triango com as médidas informadas!!')
else:
    print('Com as médidas informadas não é possivel forma um triangulo!!')
