from graphics import *
from other_tools import *
import musica

from MarioBros.reference import *

import pygame
import time
def verificarEvento_redimension(event):
    if event.type == pygame.VIDEORESIZE:
        resize(event.w, event.h)
        try:
            windowResizing(event) 
        except: pass           
def verificarEvento_salir(event):
    if event.type == pygame.QUIT:
        try:
            windowClosing() 
        except: pass
def verificarEventos_teclado(event):
    try:
        KeyPressed(event) 
    except: pass
    try:
        KeyReleased(event) 
    except: pass
        
def verificarEventos_mouse(event):
    try:
        MousePressed(event) 
    except: pass
    try:
        MouseReleased(event) 
    except: pass
    try:
        MouseMotion(event) 
    except: pass 
def verificarEventos():
    for event in pygame.event.get():
        verificarEvento_salir(event)
        verificarEvento_redimension(event)
        verificarEventos_teclado(event)
        verificarEventos_mouse(event)
descanso_por_fotograma = [0]
def calibrarDescansoPorFotograma():
    c = (frameRateAverage() / frameRate()-1) / (2 * frameRate())
    descanso_por_fotograma[0] += c
    if descanso_por_fotograma[0] > 1 / frameRate():
        descanso_por_fotograma[0] = 1 / frameRate()     
def update():
    pygame.display.update()
    updateMouse() 
    if(update_fps()):
        calibrarDescansoPorFotograma()
    verificarEventos()
if __name__ == '__main__':
    descanso_por_fotograma[0] = 1 / frameRate() 
    try: 
        setup() 
    except: printErr("setup() no se ha podido completar correctamente")
    
    while enEjecucion():
        inicioCicloFotograma = time.time()
        update() 
        resetGraphics() 
        draw() 
        pygame.display.flip()
        duracion_cicloFotograma = time.time()-inicioCicloFotograma
        descansar = descanso_por_fotograma[0]-duracion_cicloFotograma
        if(descansar > 0):
            time.sleep(descansar)