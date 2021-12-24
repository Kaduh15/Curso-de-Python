"""Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

largura = float(input('Lagura do parede: '))
altura = float(input('Altura da parede: '))

area_da_parede = largura * altura
latas_de_tinta = area_da_parede / 2

print(f'Uma parede {altura}x{largura} tem {area_da_parede}m² e precisa de {latas_de_tinta} latas de tinta para ser pintada.')
