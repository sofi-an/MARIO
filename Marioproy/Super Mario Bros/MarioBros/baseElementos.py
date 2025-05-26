from MarioBros.reference import *
from graphics import *

unidad = 40

def buscarInterseccion(rect, obj):
    for objetos in objetosColisionables:
        for o in objetos:
            if(isinstance(obj, Jugador)):
                if(objetos == hongos):
                    continue
            if(obj == o):
                continue
            if(rect.colliderect(o.rect())):
                return [rect.clip(o.rect()), o]
    return [null, null]

class Dibujable:
    
    x = 0
    y = 0
    w = unidad
    h = unidad
    
    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    def fueraDeVista(self):
        p = transformPoint((self.x, self.y))
        if(p[0]  < -4 * unidad - self.w or p[0]  > 20 * unidad + self.w):
            return true
        
class Interactuable(Dibujable):
    
    dx = 0
    dy = 0
    
    dibujar_rects = false
    
    def ignorarColision(self):
        return false
    
    def intersect_piso(self):
        return buscarInterseccion(self.rect_piso(), self)
    
    def rect_piso(self):
        r = self.rect()
        r.y = r.bottom
        r.h = 1
        return r
    
    def rect_abajo(self):
        r = self.rect()
        if(self.dy > 0):
            r.y = r.bottom-r.h * .7 + self.dy
        else:
            r.y = r.bottom-r.h * .7
        r.h *= .7
        return r
    
    def rect_arriba(self):
        r = self.rect()
        if(self.dy < 0):
            r.y += self.dy - 3
        else:
            r.y -= 3
        r.h *= .7
        return r
    
    def rect_derecha(self):
        r = self.rect()
        if(self.dx > 0):
            r.x = r.right-r.w / 2 + self.dx + 3
        else:
            r.x = r.right-r.w / 2 + 3
        r.w = r.w / 2
        return r
    
    def rect_izquierda(self):
        r = self.rect()
        if(self.dx < 0):
            r.x += self.dx - 3 
        else:
            r.x -= 3 
        r.w = r.w / 2
        return r
    
    def dibujarRectangulosInteraccion(self):
        color(0xff)
        rect(self.rect_izquierda(), false)
        rect(self.rect_derecha(), false)
        color(0xff0000)
        rect(self.rect(), false)
        color(0xff00)
        rect(self.rect_arriba(), false)
        rect(self.rect_abajo(), false)
        
class Caminante(Interactuable):
    
    elasticidad = 0
    dx = 0
    dy = 0
    max_dx = 2
    min_dx = -max_dx
    caer = true
    mirarDerecha = false
    saltarEnMuerte = false
    
    def ignorarColision(self):
        return self.saltarEnMuerte
    
    def __init__(self, x=2.5 * unidad, y=12 * unidad, imagen=null):
        self.x = x
        self.y = y
        self.imagen = imagen
        
    def efectoSaltarEnMuerte(self):
        self.saltarEnMuerte = true
        self.dy = -5
        self.dx *= 2
    
    def colisionArriba(self):
        return buscarInterseccion(self.rect_arriba(), self)
    
    def colisionDerecha(self):
        colision = buscarInterseccion(self.rect_derecha(), self)
        obj = colision[1]
        if obj != null and obj.ignorarColision():
            return [null, null]
        return colision             

    def colisionAbajo(self):
        colision = buscarInterseccion(self.rect_abajo(), self)
        obj = colision[1]
        if obj != null and obj.ignorarColision():
            return [null, null]
        return colision     
    
    def colisionIzquierda(self):
        colision = buscarInterseccion(self.rect_izquierda(), self)
        obj = colision[1]
        if obj != null and obj.ignorarColision():
            return [null, null]
        return colision             
    
    def Caer(self):
        colision = self.intersect_piso()
        obj = colision[1]
        if obj != null and obj.ignorarColision():
            return [null, null]
        return colision[0] == null             
        
    def acelerar(self):
        self.x = self.x + int((self.dx) * 100) / 100
        self.y = self.y + int((self.dy) * 100) / 100
        
    def evt_colision_derecha(self, colision):
        intersect = colision[0]
        obj = colision[1]
        self.BuscarAtaque(obj)
        self.cambiarSentido(intersect, obj)
        self.BuscarChoqueJugador(intersect, obj)
        
    def evt_sin_colision_derecha(self):
        if(self.dx > 0):
            if(self.Caer()):
                self.dx += .5 
            else:
                self.dx += .3 
            if(self.dx >= self.max_dx):
                self.dx = self.max_dx
        
    def evt_colision_izquierda(self, colision):
        intersect = colision[0]
        obj = colision[1]
        self.BuscarAtaque(obj)
        self.cambiarSentido(intersect, obj)
        self.BuscarChoqueJugador(intersect, obj)
        
    def BuscarChoqueJugador(self, intersect, obj):
        if(isinstance(obj, Jugador)):
            if(isinstance(self, Estrella)):
                self.adquirido = true
            if(isinstance(self, Hongo)):
                obj.crecer()
                self.adquirido = true
        
    def BuscarAtaque(self, obj):
        if(not isinstance(self, Enemigo)):
            return
        if(isinstance(obj, Jugador)):
            obj.atacar()
            if(obj.x < self.x):
                obj.x -= unidad
            else:
                obj.x += unidad
            obj.dx = 0
        
    def cambiarSentido(self, intersect, obj):
        if(self.mirarDerecha):
            self.x -= intersect.w
            self.mirarDerecha = false
            self.dx = -.1
        else:
            self.x += intersect.w
            self.mirarDerecha = true
            self.dx = .1
        
    def evt_sin_colision_izquierda(self):
        if(self.dx < 0):
            if(self.Caer()):
                self.dx -= .5 
            else:
                self.dx -= .3 
            if(self.dx <= -self.min_dx):
                self.dx = self.min_dx
            
    def evt_colision_abajo(self, colision):
        intersect = colision[0]
        obj = colision[1]
        self.dy = int(self.dy * -self.elasticidad * 10) / 10
        if(self.Caer()):
            self.y = obj.rect().y-self.h
        else:
            self.y -= 1 
        self.BuscarChoqueJugador(intersect, obj)
        
    def evt_sin_colision_abajo(self):
        if(self.Caer()):
            self.dy += .3 
            if(self.dy > 15):
                self.dy = 15
                
    def evt_colision_arriba(self, colision):
        intersect = colision[0]
        obj = colision[1]
        self.BuscarChoqueJugador(intersect, obj)
        
    def evt_sin_colision_arriba(self):
        pass
            
    def evts_abajo(self):
        colision = self.colisionAbajo()
        intersect = colision[0]
        obj = colision[1]
        if(intersect == null or self.saltarEnMuerte):
            try:  self.evt_sin_colision_abajo()
            except: printErr("Error en el evento: colison abajo")
        else:
            try:  self.evt_colision_abajo(colision)
            except: printErr("Error en el evento: colison abajo")
        
    def evts_izquierda(self):
        colision = self.colisionIzquierda()
        intersect = colision[0]
        if(intersect == null or self.saltarEnMuerte):
            try: self.evt_sin_colision_izquierda()
            except: printErr("Error en el evento de SIN colision a la izquierda")
        else:
            try: self.evt_colision_izquierda(colision)
            except: printErr("Error en el evento de colision a la izquierda")
            
    def evts_derecha(self):
        colision = self.colisionDerecha()
        intersect = colision[0]
        if(intersect == null or self.saltarEnMuerte):
            try: self.evt_sin_colision_derecha()
            except: printErr("Error en el evento de SIN colision a la derecha")
        else:
            try: self.evt_colision_derecha(colision)
            except: printErr("Error en el evento de colision a la derecha")
        
    def evts_arriba(self):
        colision = self.colisionArriba()
        intersect = colision[0]
        obj = colision[1]
        if(intersect == null or self.saltarEnMuerte):
            try: self.evt_sin_colision_arriba()
            except: printErr("Error en el evento: sin colison arriba")
        else:
            try: self.evt_colision_arriba(colision)
            except: printErr("Error en el evento: colison arriba")
            
    def evts_cardinales(self):
        self.evts_abajo()
        self.evts_derecha()
        self.evts_izquierda()
        self.evts_arriba()

    def mover(self):
        self.acelerar()
        self.evts_cardinales()
        
class Enemigo(Caminante):   
    
    max_dx = 2
    min_dx = -max_dx
    
    momentoAplastamiento = -1
    duracionAplastamiento = .7
    
    def eliminar(self):
        if(self.y > 20 * unidad):
            return true
        return false
    
    def tiempo_aplastado(self):
        if(not self.estaAplastado()):
            return 0
        return seconds()-self.momentoAplastamiento
    
    def estaAplastado(self):
        return self.momentoAplastamiento != -1
    
    def aplastar(self):
        self.dx = 0
        if(not self.estaAplastado()):
            self.momentoAplastamiento = seconds()
            
from MarioBros.actores import *