"""Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. """

dinheiro = float(input('Quanto dinheiro você tem na certeira? R$'))

print(f'Com R${dinheiro} você pode comprar US${dinheiro / 5.68:.2f}')
