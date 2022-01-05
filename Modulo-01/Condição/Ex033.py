"""Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite putro número: '))
num3 = int(input('Digite mais um número: '))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
elif num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
elif num3 < menor:
    menor = num3

print(f'O maior número foi {maior} e o menor foi {menor}')
