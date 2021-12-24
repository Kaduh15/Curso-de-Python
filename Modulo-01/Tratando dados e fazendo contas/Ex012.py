"""Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

produto = float(input('Qual o preço do produto? R$'))

desconto = produto * 0.05

print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai ficar R${(produto - desconto):.2f}')
