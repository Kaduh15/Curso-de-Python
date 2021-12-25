"""Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias_alugado = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos KM rodados? '))

preco_por_dia = dias_alugado * 60
preco_por_km = km_rodados * 0.15

valor_total = preco_por_dia + preco_por_km

print(f'O carro alugado por {dias_alugado} e com {km_rodados}km rodados.')
print(f'Valor a pagar: R${valor_total:.2f} reais')
