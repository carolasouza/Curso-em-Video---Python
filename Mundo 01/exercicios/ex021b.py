import pygame
print('===== DESAFIO 21 =====')
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('AULA 3 EM ÁUDIO.mp3')
pygame.mixer.music.play()
pygame.event.wait()
