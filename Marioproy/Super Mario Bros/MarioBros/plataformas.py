from graphics import *
from MarioBros.reference import *
from MarioBros.baseElementos import *

class Tubo(Interactuable):
    
    w = 2 * unidad
    h = 5 * unidad
    
    def __init__(self, x, y):
        self.x = x * unidad
        self.y = y * unidad
        
    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    def dibujar(self):
        if(self.fueraDeVista()):
            return
        drawImage(gestorImagenes.cabezaTubo, self.x, self.y)
        for i in range(4):
            drawImage(gestorImagenes.cuerpoTubo, self.x, self.y + (i + 1) * unidad)
            
class Piso(Interactuable):
    
    def __init__(self, x, y, w, h, img=null):
        self.x = x * unidad
        self.y = y * unidad
        self.w = w * unidad
        self.h = h * unidad
        if(img == null):
            img = gestorImagenes.piso
        self.img = img
    
    def dibujar(self):
        if(self.fueraDeVista()):
            return
        color(0, true)
        texture(self.img)
        rect(self.x, self.y, self.w, self.h, true)
        noTexture()