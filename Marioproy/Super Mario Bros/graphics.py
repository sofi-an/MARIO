import os
import pygame
import pygame.gfxdraw
import time
true = True 
false = False
none = None
null = None
pygame.init() 
os.environ['SDL_VIDEO_CENTERED'] = '1' 
canvas = [pygame.display.set_mode([640, 480], pygame.RESIZABLE)] 
mainCanvas = [null] 
canvasResizable = [True] 
fps = [60] 
colorDefeatPaint = [0, 0, 0, 255]
fontDefeatPaint = ["arial", 18, false, false]
strokePaint = [1] 
radioPointG = [2] 
colorPaint = [colorDefeatPaint[0], colorDefeatPaint[1], colorDefeatPaint[1], 255] 
texturePaint = [null] 
fontPaint = [
pygame.font.SysFont(fontDefeatPaint[0], fontDefeatPaint[1]), 
    fontDefeatPaint[0], 
    fontDefeatPaint[1]
]
def resetGraphics():
    color(colorDefeatPaint)
    fd = font_defeat()
    name_font = fd[0]
    sz_font = fd[1]
    bld_font = fd[2]
    itlc_font = fd[3]
    font(pygame.font.SysFont(name_font, sz_font, bld_font, itlc_font))
    stroke(1)
    radioPoint(2)
    transform().resetTransform()
    toMainCanvas()
    circleMode(CIRCLE_MODE_CENTER)
    noTexture()
def texture(img=null):
    if(img is not null):
        texturePaint[0] = img
    else:
        return texturePaint[0]
def noTexture():
    texturePaint[0] = null
def haveTexture():
    return texturePaint[0] is not null
def colorDefeat(r=null, g=null, b=null, a=null):
    if(r is not null):
        c = generateColorTuple(r, g, b, a)
        colorDefeatPaint[0] = c[0]
        colorDefeatPaint[1] = c[1]
        colorDefeatPaint[2] = c[2]
        colorDefeatPaint[3] = c[3]
    else:
        return colorDefeatPaint
def color(r=null, g=null, b=null, a=null):
    if(r is not null):
        c = generateColorTuple(r, g, b, a)
        colorPaint[0] = c[0]
        colorPaint[1] = c[1]
        colorPaint[2] = c[2]
        colorPaint[3] = c[3]
    else:
        return colorPaint
def generateColorTuple_hex(argb, alpha=false):
    retorno = [0, 0, 0, 0]
    retorno[0] = (argb >> 16) & 0xff
    retorno[1] = (argb >> 8) & 0xff
    retorno[2] = argb & 0xff
    if alpha:
        retorno[3] = (argb >> 24) & 0xff
    else:
        retorno[3] = 255
    return retorno
def generateColorTuple_rgba(r, g=null, b=null, a=255):
    retorno = [0, 0, 0, 0]
    if(isinstance(r, (list, pygame.Color))):
        retorno[0] = r[0]
        retorno[1] = r[1]
        retorno[2] = r[2]
        if(len(r) == 4):
            retorno[3] = r[3]
    else:
        retorno[0] = r
        retorno[1] = g
        retorno[2] = b
    retorno[3] = a
    return retorno
def generateColorTuple(r=null, g=null, b=null, a=null):
    if(r is not null):
        if(isinstance(r, (list, pygame.Color))):
            return generateColorTuple_rgba(r)
        if(b is null):
            argb = r
            alpha = false
            if(g is not null):
                alpha = g
            return generateColorTuple_hex(argb, alpha)
        else:
            return generateColorTuple_rgba(r, g, b, a)
def isColorTransparent():
    return colorPaint[3] < 255
def noColor():
    return colorPaint[3] == 0
def radioPoint(r=null):
    if(r is not null):
        radioPointG[0] = r
    else:
        return int(radioPointG[0])
def stroke(w=null):
    if(w is not null):
        strokePaint[0] = w
    else:
        return strokePaint[0]
ejecutar = [True]

fpsa = [fps[0]]
contador_fps = [0]
ultimaActualizacion_fps = [time.time()]
def frameRateAverage():
    return fpsa[0]
def update_fps():
    tiempoTranscurrido = time.time()-ultimaActualizacion_fps[0] 
    if(tiempoTranscurrido >= 1 / 2):
        fpsa[0] = (frameRateAverage() + contador_fps[0] / tiempoTranscurrido) / 2
        fpsa[0] = int(frameRateAverage() * 100) / 100
        contador_fps[0] = 0
        ultimaActualizacion_fps[0] = time.time()
        return true
    else:
        contador_fps[0] += 1
        return false
def frameRate(framespersecond=null):
    if(framespersecond is null):
        return fps[0]
    fps[0] = framespersecond
def enEjecucion():
    return ejecutar[0]
def exit():
    ejecutar[0] = false
def resize(w=840, h=800):
    if(isResizable()):
        mainCanvas[0] = pygame.display.set_mode([w, h], pygame.RESIZABLE)
    else:
        mainCanvas[0] = pygame.display.set_mode([w, h])
def title(str=null):
    if(str is null):
        return pygame.display.get_caption()
    pygame.display.set_caption(str)
def resizable(bln=true):
    canvasResizable[0] = bln
def isResizable():
    return canvasResizable[0]
def getMainCanvas():
    return mainCanvas[0]
def toMainCanvas():
    canvasActual(getMainCanvas())
def canvasActual(newCanvas=null):
    if(newCanvas is not null):
        canvas[0] = newCanvas 
    else:
        return canvas[0] 
def height():
    return canvasActual().get_width()
def width():
    return canvasActual().get_height()
def canvasDimension():
    return [width(), height()]
def paintOtherCanvas(otherCanvas, x, y):
    canvasActual().blit(otherCanvas, [x, y])
def pixel(x, y, color=null):
    if(color is not null):
        canvasActual().set_at((x, y), color)
    else:
        return canvasActual().get_at((x, y))  
def createNewCanvas(ancho, alto):
    return pygame.Surface((ancho, alto), pygame.SRCALPHA)
pmouse = [0, 0] 
mouse = [0, 0] 
def updateMouse():
    pos_pmouse(pos_mouse())
    pos = pygame.mouse.get_pos()
    pos_mouse(pos)
def pos_mouse(pos=null):
    if(pos is not null):
        mouse[0] = pos[0]
        mouse[1] = pos[1]
    else:
        return mouse
def pos_pmouse(pos=null):
    if(pos is not null):
        pmouse[0] = pos[0]
        pmouse[1] = pos[1]
    else:
        return pmouse
def mouseX():
    return mouse[0]
def mouseY():
    return mouse[1]
def pmouseX():
    return pmouse[0]
def pmouseY():
    return pmouse[1]
def mouseTX():
    return getMouseTransform()[0]
def mouseTY():
    return getMouseTransform()[1]
def pmouseTX():
    m = transformInversePoint(pmouse)
    return m[0]
def pmouseTY():
    m = transformInversePoint(pmouse)
    return m[1]
def getMouseTransform():
    return transformInversePoint(mouse)
def getSpeedMouse():
    return distance(mouseX(), mouseY(), pmouseX(), pmouseY())
def background(rgba, alpha=false):
    if(alpha):
        color(rgba, alpha)
        pygame.gfxdraw.box(canvasActual(), (0, 0, width(), height()), color())
    else:
        canvasActual().fill(rgba)
def drawImage(imagen, x, y):
    p = transformPoint([x, y])
    paintOtherCanvas(imagen, p[0], p[1])
CIRCLE_MODE_RECT = 0
CIRCLE_MODE_CENTER = 1
circleModePaint = [CIRCLE_MODE_CENTER]
def circleMode(mode=null):
    if(mode is not null):
        circleModePaint[0] = mode
    else:
        return circleModePaint[0]
def drawCircle(x, y, r):
    if(r <= 0):
        return
    pygame.draw.circle(canvasActual(), colorPaint, transformPoint_int([x, y]), int(r * getScaleX()), stroke())
def circle(x, y, r, fill=true):
    if(r <= 0):
        return
    dx = 0
    dy = 0
    if(circleMode() == CIRCLE_MODE_RECT):
        dx = r
        dy = r  
    pygame.draw.circle(canvasActual(), colorPaint, transformPoint_int([x + dx, y + dy]), int(r * getScaleX()))
def line(x1, y1, x2, y2):
    pygame.draw.line(canvasActual(), colorPaint, transformPoint_int([x1, y1]), transformPoint_int([x2, y2]), stroke())
def point(x, y):
    pygame.draw.circle(canvasActual(), colorPaint, transformPoint_int([x, y]), radioPoint())
def straight(x1, y1, x2, y2):
    t = [x2 - x1, y2 - y1]
    t = transform().rotatePoint(t)
    Vertical = direccionCardinal(t[0], t[1])[0] == 0
    p = [0, 0]
    a = [0, 0]
    b = [0, 0]
    if (Vertical):
        a = transformInversePoint([0, 0])
        b = transformInversePoint([10, 0])
    else:
        a = transformInversePoint([0, 0])
        b = transformInversePoint([0, 10])
    t1 = proporcionChoque(x1, y1, x2, y2, a[0], a[1], b[0], b[1])
    p = [(x2 - x1) * t1 + x1, (y2 - y1) * t1 + y1]
    point(p[0], p[1])
    p2 = [0, 0]
    c = [0, 0]
    d = [0, 0]
    if (Vertical):
        c = transformInversePoint([0, height()])
        d = transformInversePoint([10, height()])
    else:
        c = transformInversePoint([width(), 0])
        d = transformInversePoint([width(), 10])
    t2 = proporcionChoque(x1, y1, x2, y2, c[0], c[1], d[0], d[1])
    p2 = [(x2 - x1) * t2 + x1, (y2 - y1) * t2 + y1]
    point(p2[0], p2[1])
    line(p[0], p[1], p2[0], p2[1])
def averagePoints(points):
    retorno = [0, 0]
    for punto in points:
        retorno[0] += punto[0]
        retorno[1] += punto[1]
    retorno[0] /= len(points)
    retorno[1] /= len(points)
    return retorno
def drawPolygon(dots):
    newdots = []
    for dot in dots:
        if isColorTransparent():
            newdots.append(transformPoint(dot))
        else:
            newdots.append(transformPoint_int(dot))
    if isColorTransparent():
        pygame.gfxdraw.polygon(canvasActual(), newdots, colorPaint)
    else:
        pygame.draw.polygon(canvasActual(), colorPaint, newdots, stroke())

def fillPolygon(dots, img=null, tx=0, ty=0):
    colorPolygon(dots)
    texturePolygon(dots, img, tx, ty)
def colorPolygon(dots):
    if noColor():
        return
    newdots = []
    for dot in dots:
        newdots.append(transformPoint(dot))
    pygame.gfxdraw.filled_polygon(canvasActual(), newdots, colorPaint)
textureOffsetPaint = [0, 0]
def textureOffset(x=null, y=null):
    if(x is null):
        return textureOffsetPaint
    elif(y is null):
        textureOffset(x, x)
    else:
        textureOffsetPaint[0] = x
        textureOffsetPaint[1] = y
def textureOffsetX(x=null):
    if(x is null):
        return int(textureOffsetPaint[0])
    else:
        textureOffsetPaint[0] = x
        
def textureOffsetY(y=null):
    if(y is null):
        return int(textureOffsetPaint[1])
    else:
        textureOffsetPaint[1] = y

def texturePolygon(dots, img=null, tx=0, ty=0):
    if(img is not null):
        texture(img)
    if not haveTexture():
        return
    newdots = []
    for dot in dots:
        newdots.append(transformPoint(dot))
    try:
        pygame.gfxdraw.textured_polygon(canvasActual(), newdots, texture(), textureOffsetX(), textureOffsetY())
    except:
        pass

def rect(x=null, y=null, w=null, h=null, fill=true):
    if(type(x) == pygame.Rect):
        r = x
        if(y is not null):
            fill = y
        x = r.x
        y = r.y
        w = r.w
        h = r.h
    r = pygame.Rect(x, y, w, h)
    p1 = r.topleft
    p2 = r.topright
    p3 = r.bottomright
    p4 = r.bottomleft
    if fill:
        fillPolygon([p1, p2, p3, p4])
    else:
        drawPolygon([p1, p2, p3, p4])

def drawTriangle(x1, y1, x2, y2, x3, y3):
    drawPolygon([[x1, y1], [x2, y2], [x3, y3]])

def fillTriangle(x1, y1, x2, y2, x3, y3):
    fillPolygon([[x1, y1], [x2, y2], [x3, y3]])

def lines(dots):
    c = 0
    p1 = [0, 0]
    for dot in dots:
        if(c % 2 == 0):
            p1 = dot
        else:
            line(p1[0], p1[1], dot[0], dot[1])
        c = (c + 1)

def drawTriangles(dots):
    c = 0
    p1 = [0, 0]
    p2 = [0, 0]
    for dot in dots:
        if(c % 3 == 0):
            p1 = dot
        elif(c % 3 == 1):
            p2 = dot
        else:
            drawTriangle(p1[0], p1[1], p2[0], p2[1], dot[0], dot[1])
        c = (c + 1)

def fillTriangles(dots):
    c = 0
    p1 = [0, 0]
    p2 = [0, 0]
    for dot in dots:
        if(c % 3 == 0):
            p1 = dot
        elif(c % 3 == 1):
            p2 = dot
        else:
            fillTriangle(p1[0], p1[1], p2[0], p2[1], dot[0], dot[1])
        c = (c + 1)

def drawTrianglesStrip(dots):
    c = 0
    p1 = [0, 0]
    p2 = [0, 0]
    p3 = [0, 0]
    for dot in dots:
        if(c % 3 == 0):
            p1 = dot
        elif(c % 3 == 1):
            p2 = dot
        elif(c % 3 == 2):
            p3 = dot
        if(c >= 2):
            drawTriangle(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
        c = (c + 1)

def fillTrianglesStrip(dots):
    c = 0
    p1 = [0, 0]
    p2 = [0, 0]
    p3 = [0, 0]
    for dot in dots:
        if(c % 3 == 0):
            p1 = dot
        elif(c % 3 == 1):
            p2 = dot
        elif(c % 3 == 2):
            p3 = dot
        if(c >= 2):
            fillTriangle(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
        c = (c + 1)

def dots(dots):
    for dot in dots:
        point(dot[0], dot[1])

def polyline(dots):
    newdots = []
    for dot in dots:
        newdots.append(transformPoint(dot))
    pygame.draw.lines(canvasActual(), colorPaint, False, newdots, stroke())
    

def tabPressed():
    return isKeyPressed(pygame.K_TAB)

def rightPressed():
    return isKeyPressed(pygame.K_RIGHT)

def leftPressed():
    return isKeyPressed(pygame.K_LEFT)

def upPressed():
    return isKeyPressed(pygame.K_UP)

def downPressed():
    return isKeyPressed(pygame.K_DOWN)

def spacePressed():
    return isKeyPressed(pygame.K_SPACE)
    
def isKeyPressed(ascii=0):
    return pygame.key.get_pressed()[ascii]

def leftMousePressed():
    return isMousePressed(0)

def scrollMousePressed():
    return isMousePressed(1)

def rightMousePressed():
    return isMousePressed(2)

def isMousePressed(button=0):
    return pygame.mouse.get_pressed()[button]

def fi_flip(imagen, flipX=true, flipY=false):
    return pygame.transform.flip(imagen, flipX, flipY)

def fi_scale(imagen, w=-1, h=-1):
    if(w != -1):
        if(h != -1):
            return pygame.transform.scale(imagen, (int(w), int(h)))
        else:
            p = w / imagen.get_width()
            nh = imagen.get_height() * p
            return fi_scale(imagen, w, nh)
    else:
        if(h != -1):
            p = h / imagen.get_height()
            nw = imagen.get_width() * p
            return fi_scale(imagen, nw, h)
    return pygame.transform.scale(imagen, (imagen.get_width(), imagen.get_height()))

def fi_reemplazarCoincidencia(imagen, busqueda, reemplazo=0, posPixelBusqueda=null, posPixelReemplazo=null):
    
    if(posPixelBusqueda is not null):
        busqueda = imagen.get_at(posPixelBusqueda)
    if(posPixelReemplazo is not null):
        reemplazo = imagen.get_at(posPixelReemplazo)
        
    busqueda = generateColorTuple(busqueda)
    reemplazo = generateColorTuple(reemplazo)
    
    w = imagen.get_width()
    h = imagen.get_height()
    retorno = createNewCanvas(w, h)
    print("w")
    print(w)
    print("h")
    print(h)
    for c in range(w):
        for f in range(h):
            rgba = imagen.get_at((c, f))
            coincidencia = true
            distancia = 0;
            for i in range(4):
                comp = rgba[i] - busqueda[i]
                distancia += comp * comp
            distancia = math.sqrt(distancia)
            coincidencia = distancia < 90
            if(coincidencia):
                rgba = reemplazo
            retorno.set_at((c, f), rgba)
    return retorno

def fi_apagarCanales(imagen, dr, dg, db):
    w = imagen.get_width()
    h = imagen.get_height()
    retorno = createNewCanvas(w, h)
    for c in range(w):
        for f in range(h):
            rgba = imagen.get_at((c, f))
            rgba[0] = int(rgba[0] * dr)
            rgba[1] = int(rgba[1] * dg)
            rgba[2] = int(rgba[2] * db)
            retorno.set_at((c, f), rgba)
    return retorno

ESCALA_DE_GRISES_ROJO = 0
ESCALA_DE_GRISES_VERDE = 1
ESCALA_DE_GRISES_AZUL = 2
ESCALA_DE_GRISES_PROMEDIO_RGB = 3

def fi_escalaDeGrises(imagen, escala=ESCALA_DE_GRISES_PROMEDIO_RGB):
    w = imagen.get_width()
    h = imagen.get_height()
    retorno = createNewCanvas(w, h)
    for c in range(w):
        for f in range(h):
            rgba = imagen.get_at((c, f))
            r = rgba[0]
            g = rgba[1]
            b = rgba[2]
            g = 0
            if(escala == ESCALA_DE_GRISES_ROJO):
                g = r
            elif(escala == ESCALA_DE_GRISES_VERDE):
                g = g
            elif(escala == ESCALA_DE_GRISES_AZUL):
                g = b
            elif(escala == ESCALA_DE_GRISES_PROMEDIO_RGB):
                g = (r + g + b) // 3
            for i in range(3):
                rgba[i] = g
            retorno.set_at((c, f), rgba)
    return retorno

from graphics_text import *
from graphics_transform import *