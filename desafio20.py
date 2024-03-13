#Faça um programa em python que abra e reproduza um arquivo em MP3
import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('d20.mp3')
pygame.mixer_music.play()
input()
pygame.event.wait()