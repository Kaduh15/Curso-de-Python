"""Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

salario_atual = float(input('Digite o salario atual: R$'))

novo_salario = (salario_atual * 0.15) + salario_atual

print(f'Um funcionário que ganhava R${salario_atual}, com 15% de aumento, passa a receber R${novo_salario:.2f}')
