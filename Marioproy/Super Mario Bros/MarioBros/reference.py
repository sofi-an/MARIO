from custom_math import *
from file_management import *
from graphics import *
import math
from other_tools import *

gestorImagenes = comodin()

jugador = []
piso = []
tubos = []
cajas = []
patronesDeFondo = []
enemigos = []
hongos = []
animaciones = []

objetosColisionables = [piso, tubos, cajas, jugador, enemigos, hongos]

ESCENARIO_MENU = 0
ESCENARIO_JUEGO = 1

escenario = [ESCENARIO_MENU]

def windowClosing():
    print("\n\n\nAdios...")
    exit()

def setup():   
    title("MARIO BROS")
    folderFiles("MarioBros/Archivos")
    resizable(false)
    resize(unidad * 16, unidad * 15)
    
    jugador.clear()
    j = Jugador()
    jugador.append(j)
    
    cargaImagenes()
    cargarNivel1()
    
def draw():
    background(0x5C94FC)
    moverMapa()
    
    #dibujarCeldas()
    for e in patronesDeFondo:
        e.dibujar()
    dibujarAnimaciones()
    for t in tubos:
        t.dibujar()
    for e in piso:
        e.dibujar()
    for e in cajas:
        e.dibujar()
        
    eliminarHongos = []        
    for e in hongos:
        e.dibujar()
        if(e.eliminar()):
            eliminarHongos.append(e)
    for e in eliminarHongos:
        hongos.remove(e)
        
    dibujarEnemigos()
    jugador[0].dibujar()
    
    font_size(20)
    font_name("consolas")
    color(0)
    drawText(estadoJugador(), 2, 2, izquierda, false)
    color(0xffffff)
    drawText(estadoJugador(), 0, 0, izquierda, false)

def dibujarEnemigos():
    eliminarEnemigos = []        
    for e in enemigos:
        if(e.eliminar()):
            eliminarEnemigos.append(e)
        e.dibujar()
    for e in eliminarEnemigos:
        enemigos.remove(e)
        color(0xffffff)
        font_size(24)
        animaciones.append(animacion(
                           e.x, e.y, e.x, e.y-2 * unidad, 
                           1, 
                           "100", [unidad, -1], 
                           ANIMACION_TIPO_TEXTO
                           ))

def dibujarAnimaciones():
    eliminarAnimaciones = []
    for e in animaciones:
        if(e.eliminar()):
            eliminarAnimaciones.append(e)
        e.dibujar()
    for e in eliminarAnimaciones:
        animaciones.remove(e)
        if(e.tipo == ANIMACION_TIPO_MONEDA):
            color(0xffffff)
            font_size(24)
            animaciones.append(animacion(
                               e.xi, e.yi, e.xi, e.yi-2 * unidad, 
                               1, 
                               "200", [unidad, -1], 
                               ANIMACION_TIPO_TEXTO
                               ))

def reiniciar():
    jugador.clear()
    j = Jugador()
    jugador.append(j)
    enemigos.clear()
    piso.clear()
    tubos.clear()
    cajas.clear()
    patronesDeFondo.clear()
    cargarNivel1()
    
def consultarBloqueCabeceable(x, y):
    for caja in cajas:
        if(caja.x / unidad == x and caja.y / unidad == y):
            return caja
    print ("no se encontro el bloque en: " + str(x) + "," + str(y))
    
def generarDiagonal_izquierda(x, y, lado):
    for i in range(lado):
        piso.append(Piso(x + i, y + lado-i-1, 1, i + 1, gestorImagenes.piso1))
        
def generarDiagonal_derecha(x, y, lado):
    for i in range(lado):
        piso.append(Piso(x + i, y + i, 1, lado-i, gestorImagenes.piso1))
    
def estadoJugador():
    
    txt = "" 
    txt += "\n"
    return txt
        
def arribaIzquierdaVentana():
    return transformInversePoint((0, 0))

def moverMapa():
    p = arribaIzquierdaVentana()
    d = (jugador[0].x-p[0]) / unidad
    if(d > 7):
        xoff = -(d-7) * unidad
    else:
        xoff = -3
    translateX(xoff)
    textureOffsetX(xoff)
        
def dibujarCeldas():
    color(0x20000000, true)
    for i in range(width() // unidad + 1):
        for j in range(height() // unidad + 1):
            rect(i * unidad, j * unidad, unidad, unidad, false)
            
from MarioBros.baseElementos import *
from MarioBros.decorativo import *
from MarioBros.actores import * 
from MarioBros.plataformas import *
from MarioBros.bloques import *
from MarioBros.cargar import *
