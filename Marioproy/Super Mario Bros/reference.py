from graphics import *
import math

from custom_math import *
from file_management import *
from other_tools import *
def setup():    
    title("h")  
def draw():
    background(0xffffff)
    color(0)
    translate([dimCanvas[0] / 2, dimCanvas[1] / 2])
    straight(0, 0, 0, 1)
    straight(0, 0, 1, 0)
    circle(mouseTX(), mouseTY(), getSpeedMouse())
    txt = "fps: " + str(frameRateAverage())
    drawText(txt, 2, 2, izquierda, false)
     
def KeyPressed(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT: 
            pass
        if event.key == pygame.K_LEFT: 
            pass
        if event.key == pygame.K_UP: 
            pass
        if event.key == pygame.K_DOWN: 
            pass
        if event.key == pygame.K_SPACE: 
            pass 
def KeyReleased(event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT: 
            pass
        if event.key == pygame.K_LEFT: 
            pass
        if event.key == pygame.K_UP: 
            pass
        if event.key == pygame.K_DOWN: 
            pass
        if event.key == pygame.K_SPACE: 
            pass
def MousePressed(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseInWindow = event.pos
        mouseInGraphics = getMouseTransform()
        if event.button == 1:   
            pass
        if event.button == 2: 
            pass
        if event.button == 3: 
            pass
        if event.button == 4: 
            pass
        if event.button == 5: 
            pass   
def MouseReleased(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouseInWindow = event.pos
        mouseInGraphics = getMouseTransform()
        if(event.button == 1): 
            pass
        if event.button == 2: 
            pass
        if event.button == 3: 
            pass
        if event.button == 4: 
            pass
        if event.button == 5: 
            pass
            
def MouseMotion(event):
    if event.type == pygame.MOUSEMOTION:
        mouseInWindow = event.pos
        mouseInGraphics = getMouseTransform()
        if(event.buttons[0] == 1): 
            pass
        if event.buttons[1] == 1: 
            pass
        if event.buttons[2] == 1: 
            pass
                      
def windowResizing(event):
    pass

def windowClosing():
    print("Adios...")
    exit()