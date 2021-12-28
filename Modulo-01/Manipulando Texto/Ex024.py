"""Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”."""

cidade = input('Didige o nome da cidade: ').strip().upper()

print('SANTO' in cidade.split()[0])
