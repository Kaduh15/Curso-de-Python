"""Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. """

nome = input('Digite seu nome completo: ').strip().title()

print(f'Seu primeiro nome é {nome.split()[0]} e seu último nome é {nome.split()[-1]}')
