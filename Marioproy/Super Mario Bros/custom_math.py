from graphics import *
import math

arriba = 0
top = arriba
centro = 1
center = centro
abajo = 2
bottom = abajo
izquierda = 0
left = izquierda
derecha = 2
right = derecha

def center(w_envolvente, h_envolvente, w_menor=null, h_menor=null):
    return align(centro, centro, w_envolvente, h_envolvente, w_menor, h_menor)

def align(AH, AV, w_envolvente, h_envolvente, w_menor=null, h_menor=null):
    x = -1
    y = -1

    if(type(w_envolvente) == tuple):
        r1 = w_envolvente
        r2 = h_envolvente
        w_envolvente = r1[0]
        h_envolvente = r1[1]
        w_menor = r2[0]
        h_menor = r2[1]
   
    if(type(w_envolvente) == pygame.Rect):
        r1 = w_envolvente
        r2 = h_envolvente
        w_envolvente = r1.w
        h_envolvente = r1.h
        w_menor = r2.w
        h_menor = r2.h
  
    if(AH == izquierda):
        x = 0
    elif(AH == centro):
        x = (w_envolvente-w_menor) / 2
    elif(AH == derecha):
        x = w_envolvente-w_menor
    
    if(AV == arriba):
        y = 0
    elif(AV == centro):
        y = (h_envolvente-h_menor) / 2
    elif(AV == abajo):
        y = h_envolvente-h_menor
 
    return (w, y)

def toPoint_int(point):
    return [int(point[0]), int(point[1])]

def distance(x1, y1, x2=0, y2=0):
    a = x2-x1
    b = y2-y1
    return math.sqrt(a * a + b * b)

def cardinal(n):
    if (n > 0.71):
        return 1
    if (n < -0.71):
        return -1
    return 0

def direccionCardinal(x, y):
    r = math.sqrt(x * x + y * y)
    x /= r
    y /= r
    x = cardinal(x)
    y = cardinal(y)
    d = [x, y]
    return d

def determinante(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def proporcionChoque(ax, ay, bx, by, cx, cy, dx, dy):
    v1 = [bx - ax, by - ay];
    v2 = [dx - cx, dy - cy];
    v3 = [ax - cx, ay - cy];
    return -determinante(v2, v3) / determinante(v2, v1)
