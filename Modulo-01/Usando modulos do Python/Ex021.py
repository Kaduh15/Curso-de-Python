"""Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

import pygame

pygame.init()
pygame.mixer.music.load('/home/kadu/Documentos/GitHub/Curso-de-Python/Modulo-01/Usando modulos do Python/musga.mp3')
pygame.mixer.music.play()
pygame.event.wait()
