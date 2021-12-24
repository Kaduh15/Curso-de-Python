"""Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

distancia = float(input('Digite uma distância em metros: '))

print(f'A medida de {distancia}m corresponde a')
print(f'{distancia / 1000}km')
print(f'{distancia / 100}hm')
print(f'{distancia / 10}dam')
print(f'{distancia * 10}dm')
print(f'{distancia * 100}cm')
print(f'{distancia * 1000}mm')
