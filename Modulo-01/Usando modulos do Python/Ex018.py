"""Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. """

from math import sin, cos, tan, radians

angulo = int(input('Digite o valor do Ângulo: '))

seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print(f'O ângulo de {angulo}° tem o')
print(f'Seno de {seno:.2f}° Graus')
print(f'Cosseno de {coss:.2f}° Gruas')
print(f'Tangente de {tang:.2f}° Graus')
