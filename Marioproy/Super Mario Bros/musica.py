import pygame
import os

pygame.init()
pygame.mixer.init()
ruta_musica = os.path.join("MarioBros", "Archivos", "Super Mario Bros. Theme Song - ultragamemusic.mp3")
pygame.mixer.music.load(ruta_musica)
pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)
