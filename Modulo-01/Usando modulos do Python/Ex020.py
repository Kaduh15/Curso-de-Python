"""Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle

aluno1 = input('Nome do 1° Aluno: ')
aluno2 = input('Nome do 2° Aluno: ')
aluno3 = input('Nome do 3° Aluno: ')
aluno4 = input('Nome do 4° Aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

print(f'A ordem de apresentação será')
print(alunos)
