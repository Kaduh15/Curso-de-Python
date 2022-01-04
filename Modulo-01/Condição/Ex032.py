"""Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

from datetime import date

ano_atual = date.today().year

print(ano_atual)

ano = int(input('Digite o ano para saber se ele é bissexto: '))

if ano == 0:
    ano = ano_atual

if ano % 4 == 0 and int(ano / 100) % 4 == 0:
    print(f'{ano} é ano bissexto!')
else:
    print(f'{ano} não é ano bissexto!')
