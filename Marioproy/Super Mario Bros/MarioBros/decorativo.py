from graphics import *
from MarioBros.baseElementos import *

class elementoDeFondo(Dibujable):
    
    def __init__(self, x, y, imagen):
        self.x = x * unidad
        self.y = y * unidad
        self.imagen = imagen
        self.w = imagen.get_width()
        self.h = imagen.get_height()
    
    def dibujar(self):
        if(self.fueraDeVista()):
            return
        drawImage(self.imagen, self.x, self.y)
        
class patronFondo:
    
    def __init__(self, elementosFondo, RepeticionHorizontal, distancia):
        self.elementosFondo = []
        cantidadElementosFondo = len(elementosFondo)
        for i in range (RepeticionHorizontal):
            for j in range(cantidadElementosFondo):
                e = elementosFondo[j]
                self.elementosFondo.append(elementoDeFondo(e.x / unidad + i * distancia, e.y / unidad, e.imagen))
        
    def dibujar(self):
        for e in self.elementosFondo:
            e.dibujar()
            
ANIMACION_TIPO_MONEDA = 0
ANIMACION_TIPO_TEXTO = 1

class animacion(Dibujable):
    
    def __init__(self, xi, yi, xf, yf, tiempoDuracion, txt=null, img=null, tipo=ANIMACION_TIPO_MONEDA):
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
        self.tiempoDuracion = tiempoDuracion
        self.tinicio = seconds()
        if(txt != null):
            self.imagen = fi_scale(textRender(txt), img[0], img[1])
        else:
            self.imagen = img
        self.tipo = tipo
     
    def  eliminar(self):
        p = self.tiempoTranscurrido() / self.tiempoDuracion
        return (p > 1)
    
    def tiempoTranscurrido(self):
        secondsTranscurridos = seconds()-self.tinicio
        return secondsTranscurridos

    def porcentajeCaida(self):
        p = self.tiempoTranscurrido() / self.tiempoDuracion
        if(p > 1):
            p = 1
        if(self.tipo == ANIMACION_TIPO_MONEDA):
            p = math.sin(p * math.pi)
        return p
    
    def calcularPosicion(self):
        self.x = (self.xf-self.xi) * self.porcentajeCaida() + self.xi
        self.y = (self.yf-self.yi) * self.porcentajeCaida() + self.yi
        return (self.x, self.y)
    
    def dibujar(self):
        self.calcularPosicion()
        if(self.fueraDeVista()):
            return
        if(self.imagen != null):
            drawImage(self.imagen, self.x, self.y)
        else:
            color(0x55ffffff, true)
            rect(self.x, self.y, unidad, unidad)