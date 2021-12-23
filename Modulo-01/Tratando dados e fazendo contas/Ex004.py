"""Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele."""

n = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um número? {n.isnumeric()}')
print(f'É alfabético? {n.isalpha()}')
print(f'Está em maiúsculas? {n.isupper()}')
print(f'Está em minúsculas? {n.islower()}')
print(f'está caítalizada? {n.istitle()}')
