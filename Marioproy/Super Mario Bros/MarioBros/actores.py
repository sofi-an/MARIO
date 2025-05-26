from MarioBros.baseElementos import *
from MarioBros.bloques import *
from MarioBros.reference import *
from graphics import *

class Ventaja(Caminante):
        
    adquirido = false
        
    def eliminar(self):
        if(self.y > 20 * unidad):
            return true
        return self.adquirido
        
    def ignorarColision(self):
        return self.eliminar()
        
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = .1


class Estrella(Ventaja):
    
    def dibujar(self):
        if(self.fueraDeVista()):
            return
        drawImage(gestorImagenes.estrella, self.x, self.y)
        if(self.dibujar_rects):
            self.dibujarRectangulosInteraccion()
        self.mover()
        if(not self.Caer()):
            self.dy = -10
        
class Hongo(Ventaja):
    
    def dibujar(self):
        if(self.fueraDeVista()):
            return
        drawImage(gestorImagenes.hongo, self.x, self.y)
        if(self.dibujar_rects):
            self.dibujarRectangulosInteraccion()
        self.mover()

class Jugador(Caminante):
    
    grande = false

    def atacar(self):
        if(self.grande):
            self.grande = false
            self.h -= unidad
            self.y += unidad
        else:
            self.efectoSaltarEnMuerte()
    
    def intersect_cabeza(self):
        return buscarInterseccion(self.rect_cabeza(), self)
    
    def rect_cabeza(self):
        r = self.rect()
        r.y += self.dy
        r.h = r.h / 4
        r.x += (r.w-10) / 2
        r.w = 10
        return r
    
    mirarDerecha = true
    haSaltado = false
    ascender = true
    
    def crecer(self):
        if(self.grande):
            return
        self.grande = true
        self.h += unidad
        self.y -= unidad
    
    def dibujar(self):
        if(self.y > 40 * unidad):
            reiniciar()
            return
            
        imgMario = gestorImagenes.marioMini
        if(self.grande):
            imgMario = gestorImagenes.marioGrande
            
        if(self.saltarEnMuerte):
            drawImage(gestorImagenes.marioMini.salto_muerte, self.x, self.y)
        elif(self.haSaltado):
            if(self.mirarDerecha):
                drawImage(imgMario.salto_derecha, self.x, self.y)
            else:
                drawImage(imgMario.salto_izquierda, self.x, self.y)
        elif(rightPressed()):
            f = len(imgMario.caminando_derecha) - 1
            i = int(seconds() / imgMario.caminando_derecha[f]) % f
            drawImage(imgMario.caminando_derecha[i], self.x, self.y)
        elif(leftPressed()):
            f = len(imgMario.caminando_izquierda) - 1
            i = int(seconds() / imgMario.caminando_izquierda[f]) % f
            drawImage(imgMario.caminando_izquierda[i], self.x, self.y)
        else:
            if(self.mirarDerecha):
                drawImage(imgMario.quieto.derecha, self.x, self.y)
            else:
                drawImage(imgMario.quieto.izquierda, self.x, self.y)
        
        if(self.dibujar_rects):
            self.dibujarRectangulosInteraccion()
            
        self.mover()
        
    def efectoSaltarEnMuerte(self):
        self.saltarEnMuerte = true
        self.dy = -9
        self.dx *= 2
        
    def evt_colision_derecha(self, colision):
        intersect = colision[0]
        obj = colision[1]
        bajando = self.dy > 0
        if(isinstance(obj, Enemigo) and not bajando):
            aplastarTortuga = isinstance(obj, Tortuga) and obj.estaAplastado() and obj.dx == 0
            if(aplastarTortuga):
                obj.max_dx = 7
                obj.min_dx = -7
                obj.dx = 7
                obj.x += intersect.w
                self.x -= intersect.w
            else:
                pass
        else:
            self.dx = 0
        
    def evt_sin_colision_derecha(self):
        if(rightPressed() and not self.saltarEnMuerte):
            self.mirarDerecha = true
            if(self.Caer()):
                self.dx += .5 
            else:
                self.dx += .3 
            if(self.dx >= 5):
                self.dx = 5
                
    def evt_colision_izquierda(self, colision):
        intersect = colision[0]
        obj = colision[1]
        bajando = self.dy > 0
        if(isinstance(obj, Enemigo)  and not bajando):
            if(isinstance(obj, Tortuga) and obj.estaAplastado() and obj.dx == 0):
                obj.max_dx = 7
                obj.min_dx = -7
                obj.dx = -7
                obj.x -= intersect.w
                self.x += intersect.w
            else:
                pass
        else:
            self.dx = 0
        
    def evt_sin_colision_izquierda(self):
        if(leftPressed() and not self.saltarEnMuerte):
            self.mirarDerecha = false
            if(self.Caer()):
                self.dx -= .5 
            else:
                self.dx -= .3 
            if(self.dx <= -5):
                self.dx = -5
            
    def evt_colision_abajo(self, colision):
        intersect = colision[0]
        obj = colision[1]
        self.dy = int(self.dy * -self.elasticidad * 10) / 10
        self.ascender = true
        self.haSaltado = false
        if(isinstance(obj, Enemigo)):
            obj.aplastar()
            self.dy = -8
            self.haSaltado = true
        if(self.Caer()):
            self.y = obj.rect().y-self.h
        else:
            self.y -= 1 
        
    def evt_colision_arriba(self, colision):
        intersect = colision[0]
        obj = colision[1]
        
        #calibrar golpe con la cabeza
        colision = self.intersect_cabeza()
        if(colision[0] != null):
            intersect = colision[0]
            obj = colision[1]
            
        if(self.dy < -1 and isinstance(obj, (BloqueCabeceable))):
            obj.iniciarCaida()
        if(self.dy < 0):
            self.dy = 3
        
    def evt_sin_colision_arriba(self):
        if(upPressed() and not self.saltarEnMuerte):
            if(self.ascender):
                if(self.dy == 0):
                    self.dy = -5
                    self.haSaltado = true
                if(self.dy < 0):
                    self.dy *= 1.3
                if(self.dy <= -10):
                    self.ascender = false
        elif(self.Caer()):
            self.ascender = false
        
    def acelerar(self):
        self.x += self.dx
        self.y += self.dy
        if(self.saltarEnMuerte or (not rightPressed() and not leftPressed())):
            if(self.Caer()):
                self.dx *= .95 
            else:
                self.dx *= .7 

class Bowser(Enemigo):
    
    vida = 5
    
    h = 2 * unidad
    w = 2 * unidad
    
    saltar = seconds()
    saltarderecha = seconds()
    
    def __init__(self, x=2.5, y=12):
        self.x = x * unidad
        self.y = y * unidad
        
    def evt_sin_colision_derecha(self):
        pass
    
    def evt_sin_colision_izquierda(self):
        pass
    
    def aplastar(self):
        self.vida -= 1
        if(self.vida == 0):
            self.efectoSaltarEnMuerte()
        
    def dibujar(self):
        self.dx = 0
        if(seconds()-self.saltar > 6 and not self.saltarEnMuerte):
            self.saltar = seconds()
            self.dy = -7
        if(seconds()-self.saltarderecha > 10 and not self.saltarEnMuerte):
            self.saltarderecha = seconds()
            self.dy = -7
            self.x += unidad
        if(self.fueraDeVista()):
            return
        f = len(gestorImagenes.bowser) - 1
        i = int(seconds() / gestorImagenes.bowser[f]) % f
        drawImage(gestorImagenes.bowser[i], self.x, self.y)

        if(self.dibujar_rects):
            self.dibujarRectangulosInteraccion()
        
        color(0x80000000, true)
        rect(self.x, self.y-20, self.w, 10, true)
        color(0xff4000)
        rect(self.x, self.y-20, self.w * (self.vida / 5), 10, true)
        
        self.mover()
    
class Tortuga(Enemigo):
    
    h = 1.5 * unidad
    duracionAplastamiento = 3
    
    def __init__(self, x=2.5, y=12):
        self.x = x * unidad
        self.y = y * unidad
        self.dx = -.1
        
    def evt_colision_derecha(self, colision):
        intersect = colision[0]
        obj = colision[1]
        if(self.estaAplastado() and self.dx != 0 and isinstance(obj, Enemigo)):
            obj.efectoSaltarEnMuerte()
            return
        self.BuscarAtaque(obj)
        self.cambiarSentido(intersect, obj)
        
    def evt_colision_izquierda(self, colision):
        intersect = colision[0]
        obj = colision[1]
        if(self.estaAplastado() and self.dx != 0 and isinstance(obj, Enemigo)):
            obj.efectoSaltarEnMuerte()
            return
        self.BuscarAtaque(obj)
        self.cambiarSentido(intersect, obj)
        
    def desfaceY(self):
        if(not self.estaAplastado()):
            return 0
        return  unidad * .5
    
    def rect(self):
        if(self.estaAplastado()):
            return pygame.Rect(self.x, self.y + self.desfaceY(), self.w, self.h -self.desfaceY())
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    def dibujar(self):
        if(self.fueraDeVista()):
            return
        if(self.estaAplastado()):
            drawImage(gestorImagenes.tortuga_aplastada, self.x, self.y)
        else:
            if(self.mirarDerecha):
                gestorImagenes.tortuga_caminando = gestorImagenes.tortuga_caminando_derecha
            else:
                gestorImagenes.tortuga_caminando = gestorImagenes.tortuga_caminando_izquierda
            f = len(gestorImagenes.tortuga_caminando) - 1
            i = int(seconds() / gestorImagenes.tortuga_caminando[f]) % f
            drawImage(gestorImagenes.tortuga_caminando[i], self.x, self.y)
        
        if(self.dibujar_rects):
            self.dibujarRectangulosInteraccion()
            
        self.mover()
        
class Muffin(Enemigo):
    
    def eliminar(self):
        if(self.tiempo_aplastado() > self.duracionAplastamiento):
            return true
        if(self.y > 20 * unidad):
            return true
        return false
    
    def aplastar(self):
        if(not self.estaAplastado()):
            self.y += self.h / 2
            self.h /= 2
            self.momentoAplastamiento = seconds()
    
    def __init__(self, x=2.5, y=12):
        self.x = x * unidad
        self.y = y * unidad
        self.dx = -.1
    
    def dibujar(self):
        if(self.fueraDeVista()):
            return
        if(self.estaAplastado()):
            drawImage(gestorImagenes.muffin_aplastado, self.x, self.y)
            return
        f = len(gestorImagenes.muffin_caminando) - 1
        i = int(seconds() / gestorImagenes.muffin_caminando[f]) % f
        drawImage(gestorImagenes.muffin_caminando[i], self.x, self.y)
        if(self.dibujar_rects):
            self.dibujarRectangulosInteraccion()
        self.mover()
        
RECOMPENSA_MONEDA = 0            
RECOMPENSA_VIDA = 1            
RECOMPENSA_ESTRELLA = 2            
RECOMPENSA_HONGO = 3            
RECOMPENSA_FLOR = 4            

class BloqueCabeceable(Interactuable):
    
    _invisible = false
    _contadorDeUso = -1
    usada = false
    tiempoReferencia = -1
    tiempoCaida = .10
    _recompensa = RECOMPENSA_MONEDA
    
    def __init__(self, x, y, img=null):
        self.x = x * unidad
        self.y = y * unidad
        if(img == null):
            img = gestorImagenes.ladrillo
        self.imagen(img)
        
    def imagen(self, img):
        self.img = img
        if(self.img == gestorImagenes.cajaMisteriosa):
            self._contadorDeUso = 1
        return self
    
    def contadorDeUso(self, contador=null):
        if(contador == null):
            return self._contadorDeUso
        self._contadorDeUso = contador
        return self
    
    def ignorarColision(self):
        return self.invisible()
    
    def invisible(self, bln=null):
        if(bln == null):
            return self._invisible
        self._invisible = bln
        return self
    
    def tiempoTranscurridoCaida(self):
        return seconds() - self.tiempoReferencia
    
    def iniciarCaida(self):
        self.tiempoReferencia = seconds()
        self._contadorDeUso -= 1
        self.recompensar()
        if self._contadorDeUso == 0:
            self.usada = true
            self._invisible = false
              
    def recompensa(self, tipoDeRecompensa=null):
        if(tipoDeRecompensa == null):
            return self._recompensa
        self._recompensa = tipoDeRecompensa
        
    def recompensar(self):
        if(self.usada or self.contadorDeUso() < 0):
            return
        if(self.recompensa() == RECOMPENSA_HONGO):
            hongos.append(Hongo(self.x, self.y-unidad * 1.5))
        if(self.recompensa() == RECOMPENSA_ESTRELLA):
            hongos.append(Estrella(self.x, self.y-unidad * 1.5))
        if(self.recompensa() == RECOMPENSA_MONEDA):
            animaciones.append(animacion(self.x, self.y, self.x, self.y-2 * unidad, 1, null, gestorImagenes.moneda))
            
    def desfaceY(self):
        yi = -unidad / 2
        yf = 0
        return (yf-yi) * self.porcentaje() + yi
    
    def porcentaje(self):
        p = self.tiempoTranscurridoCaida() / self.tiempoCaida
        if(p > 1):
            return 1
        else:
            return p

    def rect(self):
        return pygame.Rect(self.x, self.y + self.desfaceY(), self.w, self.h)
    
    def fotograma(self):
        if(self.img == gestorImagenes.cajaMisteriosa):
            f = len(gestorImagenes.cajaMisteriosa) - 1
            i = int(seconds() / gestorImagenes.cajaMisteriosa[f]) % f
            return gestorImagenes.cajaMisteriosa[i]
        return self.img
    
    def dibujar(self):
        if self._invisible:
            return
        if(self.fueraDeVista()):
            return
        if(self.usada):
            drawImage(gestorImagenes.cajaUsada, self.x, self.y + self.desfaceY())
        else:
            drawImage(self.fotograma(), self.x, self.y + self.desfaceY())