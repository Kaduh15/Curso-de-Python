"""Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

frase = input('Digite uma frase: ').strip().lower()

ultimo_a = len(frase) - frase[::-1].find('a')

print(f'A frase tem {frase.count("a")} letras A')
print(f'O primeiro A aparece na {frase.find("a") + 1}° posição')
print(f'O último A aparece na {ultimo_a}° posição')
