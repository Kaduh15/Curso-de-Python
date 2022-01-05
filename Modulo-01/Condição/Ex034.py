""""Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Digite o valor do salário: R$'))

if salario > 1250:
    novo_salario = (salario * 0.10) + salario
else:
    novo_salario = (salario * 0.15) + salario

print(f'O novo salario é de R${novo_salario} reais')
