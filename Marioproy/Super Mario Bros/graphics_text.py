from custom_math import *
from graphics import *
from other_tools import *
import pygame

def font(name=null, sz=18, bold=False, italic=False):
    if(name is null):
        return fontPaint[0]
    if(isinstance(name, (pygame.font.Font))):
        fuente = name
        fontPaint[0] = fuente
    else:
        fontPaint[0] = pygame.font.SysFont(name, sz, bold, italic)

def setFont(name="arial", sz=18, bold=False, italic=False):
    fontPaint[1] = name
    fontPaint[2] = sz
    font(pygame.font.SysFont(name, sz, bold, italic))

def font_name(nm=null):
    if(nm is null):
        return fontPaint[1]
    setFont(nm, font_size(), font_bold(), font_italic())
    
def font_size(sz=null):
    if(sz is null):
        return fontPaint[2]
    setFont(font_name(), sz, font_bold(), font_italic())
    
def font_height():
    return font().get_height()

def heightText(): 
    return font_height()
    
def font_italic(b=null):
    if(b is null):
        return font().get_italic()
    font().set_italic(b)
    return font()
    
def font_underline(b=null):
    if(b is null):
        return font().get_underline()
    font().set_underline(b)
    return font()

def font_bold(b=null):
    if(b is null):
        return font().get_bold()
    font().set_bold(b)
    return font()

def font_defeat(name=null, sz=18, bold=False, italic=False):
    if(name is null):
        return fontDefeatPaint
    fontDefeatPaint[0] = name
    fontDefeatPaint[1] = sz
    fontDefeatPaint[2] = bold
    fontDefeatPaint[3] = italic

def metricsText(string):
    return font().size(string)

def draw_text_in_rect_center(string, w, h, AH=izquierda, AV=arriba):  
    x = (width()-w) / 2
    y = (height()-h) / 2
    paintOtherCanvas(text_in_rect(string, w, h, AH, AV), x, y)
    
def draw_text_in_rect(string, x, y, w, h, AH=izquierda, AV=arriba): 
    paintOtherCanvas(text_in_rect(string, w, h, AH, AV), x, y)
    
def text_in_rect(string, w, h, AH=izquierda, AV=arriba): 
    retorno = createNewCanvas(w, h)

    final_lines = []
    lines = string.splitlines()
        
    for requested_line in lines:
        if font().size(requested_line)[0] > w:
            words = requested_line.split(' ')
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                if font().size(test_line)[0] < w:
                    accumulated_line = test_line 
                else: 
                    final_lines.append(accumulated_line) 
                    accumulated_line = word + " " 
            final_lines.append(accumulated_line)
        else: 
            final_lines.append(requested_line) 
    
    alto = 0
    for line in final_lines:
        sz = font().size(line)
        alto += sz[1]
        
    if(AV == arriba):
        accumulated_height = 0
    elif(AV == centro):
        accumulated_height = (h-alto) / 2
    elif(AV == abajo):
        accumulated_height = (h-alto)
        
    for line in final_lines: 
        if line != "":
            tempsurface = font().render(line, true, color())
            if AH == 0:
                retorno.blit(tempsurface, (0, accumulated_height))
            elif AH == 1:
                retorno.blit(tempsurface, ((w - tempsurface.get_width()) / 2, accumulated_height))
            elif AH == 2:
                retorno.blit(tempsurface, (w - tempsurface.get_width(), accumulated_height))
                
        accumulated_height += font().size(line)[1]

    return retorno

def drawTextCenter(string, AH=izquierda): 
    txt = textRender(string, AH)
    x = (width() - txt.get_width()) / 2
    y = (height() - txt.get_height()) / 2
    paintOtherCanvas(txt, x, y)


def drawText(string, x, y, AH=izquierda, transformar=true): 
    try:
        if(not transformar):
            paintOtherCanvas(textRender(string, AH), x, y)
            return
        p = transformPoint((x, y))
        paintOtherCanvas(textRender(string, AH), p[0], p[1])
    except:
        printErr("")
   
    
def textRender(string, AH=izquierda): 
    w = 0
    h = 0
    lines = string.splitlines()
    for line in lines:
        sz = font().size(line)
        w = max(sz[0], w)
        h += sz[1]
            
    retorno = createNewCanvas(w, h)
    accumulated_height = 0 
    
    for line in lines: 
        if line != "":
            txt = font().render(line, true, color())
            if AH == 0:
                retorno.blit(txt, (0, accumulated_height))
            elif AH == 1:
                retorno.blit(txt, ((w - txt.get_width()) / 2, accumulated_height))
            elif AH == 2:
                retorno.blit(txt, (w - txt.get_width(), accumulated_height))
        accumulated_height += font().size(line)[1]

    return retorno
