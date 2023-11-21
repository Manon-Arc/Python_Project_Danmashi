import pygame
import keyboard

def jouer_musique():
    pygame.mixer.init()
    pygame.mixer.music.load("twilite.mp3")
    pygame.mixer.music.play()

jouer_musique()

while True:
    if keyboard.is_pressed('s'):
        pygame.mixer.music.stop()
        break