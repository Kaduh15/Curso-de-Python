"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

nome = input('Digite seu nome completo: ').strip()

print(f'''
Seu nome em Maiúsculas: {nome.upper()}
Seu nome em Minúsculas: {nome.lower()}
Seu nome tem {len(''.join(nome))} letras
seu primeiro nome tem {len(nome.split()[0])} letras
''')
