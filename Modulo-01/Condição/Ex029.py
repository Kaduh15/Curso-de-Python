"""Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

velocidade = int(input('Qual a velocidade do carro em Km/h? '))

if velocidade > 80:
    print('Você escedeu o limite de velocidade. Foi multado!!')
    valor_multa = (velocidade - 80) * 7
    print(f'Valor da multa de R${valor_multa} reais')
else:
    print('Você está dentro dos limites de velocidade!!')
    print('Continue assim!!!')
