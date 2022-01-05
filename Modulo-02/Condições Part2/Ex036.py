"""Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

print('-=' * 12)
print('      Banco Pyhton')
print('-=' * 12)

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos_pagar = int(input('Em quantos anos deseja pagar? '))

valor_prestacao = valor_casa / (anos_pagar * 12)
porcentagem_prestacao = (valor_prestacao * 100) / salario 

print(f'Para pagar uma casa de R${valor_casa} em {anos_pagar} anos a prestação será de R${valor_prestacao:.2f} reais!')

if porcentagem_prestacao >= 30:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo ACEITO!')
