import pygame
import time
# import subprocess#
pygame.init()
pygame.mixer.init()
#
sounda= pygame.mixer.Sound("son_caballos.wav")
#
sounda.play(20)
time.sleep (5)
sounda.stop()
