"""Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

from random import choice

aluno1 = input('Nome do 1° Aluno: ')
aluno2 = input('Nome do 2° Aluno: ')
aluno3 = input('Nome do 3° Aluno: ')
aluno4 = input('Nome do 4° Aluno: ')

print(f'O aluno sorteado foi {choice([aluno1, aluno2, aluno3, aluno4])}')
