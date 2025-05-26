from MarioBros.reference import *
from file_management import *
from graphics import *

class spriteSheet:
    
    def __init__(self, nombre, url_Imagen=null, w=-1, h=-1, url_metricas=null, columnas=1, filas=1):
        
        if(isinstance(url_Imagen, pygame.Surface)):
            self.img = url_Imagen
        else:
            self.img = loadImage(generateRoute(nombre, "png"), w, h, url_Imagen)
            
        if(url_metricas != null):
            self.matrix_tsv = matrix_tsv(url_metricas, generateRoute("metricas " + nombre + ".tsv"))
        self.columnas = columnas
        self.filas = filas
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.anchoColumna = self.w / self.columnas
        self.altoFila = self.h / self.filas
        
    def tsv(self, c, f): 
        return self.matrix_tsv[f][c]
    
    def tsv_float(self, c, f): 
        return float(self.tsv(c, f).replace(",", ".")) 
    
    def extraer_usando_tsv(self, nombre, w=-1, h=-1): 
        ruta = generateRoute(nombre, "png")
        if location_exists(ruta):
            return loadImage(ruta, w, h)
        datos = self.propiedades(nombre)
        saveImage(self.img.subsurface(datos.rect), ruta)
        return loadImage(ruta, w, h)
    
    def extraerColumna(self, columna):
        return self.img.subsurface((
                                   int(columna * self.anchoColumna),
                                   0,
                                   self.anchoColumna,
                                   self.h
                                   ))
    
    def propiedades(self, nombre): 
        fila = 0
        datos = comodin()
        try:
            while true:
                datos.nombre = self.tsv(0, fila)
                if(datos.nombre  == nombre):
                    break
                fila += 1
        except:
            printErr("error al localizar a: " + nombre)
        ancho = self.tsv_float(1, 0)
        alto = self.tsv_float(3, 0)
        xoff = 0
        woff = 0
        if(nombre == "Bowser"):
            xoff = 0.094
            woff = 0.02
        if(nombre == "Tortuga"):
            woff = 0.2
        if(nombre == "Colina"):
            xoff = 0.05
        if(nombre == "Mario Mini"):
            xoff = 0.1
        if(nombre == "Mario Grande"):
            xoff = 0.07
        if(nombre == "Bloque cabeceable (Ladrillo)"):
            xoff = 0.05
        if(nombre == "Bloque cabeceable (Usada)"):
            xoff = 0.06
        if(nombre == "Nube 1"):
            xoff = 0.06
        if(nombre == "Nube 3"):
            xoff = 0.06
        if(nombre == "Muffin"):
            woff = 0.06
        if(nombre == "Tubo (Cuerpo)"):
            woff = -0.06
            xoff = 0.05
        if(nombre == "Tubo (Cabeza)"):
            woff = 0.06
        datos.x = gestorImagenes.principal.w * (self.tsv_float(1, fila) + xoff) / ancho
        datos.y = gestorImagenes.principal.h * self.tsv_float(2, fila) / alto
        datos.w = gestorImagenes.principal.w * (self.tsv_float(3, fila) + woff)  / ancho
        datos.h = gestorImagenes.principal.h * self.tsv_float(4, fila) / alto
        datos.rect = pygame.Rect(datos.x, datos.y, datos.w, datos.h)
        return datos

def cargaImagenes():
    
    gestorImagenes.principal = spriteSheet(
                                           "imagenes", 
                                           
                                           "https://docs.google.com/drawings/d/e/2PACX-1vSnNL2lZJ40gquB08k2sFmfBv6HL-Wciv-dMPHHRLdxJgneLOrwYLohm0NqJaZTRNMJMyGq7uEJGRdr/pub?w=5000&h=100",
                                           -1, 
                                           -1, 
                                           
                                           "https://docs.google.com/spreadsheets/d/e/2PACX-1vRKx90v6MG0Rru5zfweURKX8Kn-x7hyrW3SeklO2rNoeXlmO4tLQsrgcPAxuwUSPM4jV_yK-CBPbJSw/pub?output=tsv"
                                           )
                                           
    gestorImagenes.moneda = gestorImagenes.principal.extraer_usando_tsv("Moneda", -1, unidad)
    
    gestorImagenes.marioGrande = spriteSheet(
                                             "Mario Grande", 
                                             
                                             gestorImagenes.principal.extraer_usando_tsv("Mario Grande", -1, unidad * 2),
                                             -1, 
                                             -1, 
                                             null, 
                                             21 
                                             )
                                           
    gestorImagenes.marioGrande.salto_muerte = gestorImagenes.marioGrande.extraerColumna(6)
    gestorImagenes.marioGrande.salto_derecha = gestorImagenes.marioGrande.extraerColumna(5)
    gestorImagenes.marioGrande.salto_izquierda = fi_flip(gestorImagenes.marioGrande.salto_derecha)
    
    gestorImagenes.marioGrande.quieto = comodin()
    gestorImagenes.marioGrande.quieto.derecha = gestorImagenes.marioGrande.extraerColumna(0)
    gestorImagenes.marioGrande.quieto.izquierda = fi_flip(gestorImagenes.marioGrande.quieto.derecha)
    
    gestorImagenes.marioGrande.caminando_derecha = []
    gestorImagenes.marioGrande.caminando_izquierda = []
    for i in range(3):
        img = gestorImagenes.marioGrande.extraerColumna(i + 1)
        gestorImagenes.marioGrande.caminando_izquierda.append(fi_flip(img))
        gestorImagenes.marioGrande.caminando_derecha.append(img)
    gestorImagenes.marioGrande.caminando_derecha.append(.1)
    gestorImagenes.marioGrande.caminando_izquierda.append(.1)
                                           
    gestorImagenes.marioMini = spriteSheet(
                                           "Mario Mini", 
                                           
                                           gestorImagenes.principal.extraer_usando_tsv("Mario Mini", -1, unidad),
                                           -1, 
                                           -1, 
                                           null, 
                                           14 
                                           )
    
    gestorImagenes.marioMini.salto_muerte = gestorImagenes.marioMini.extraerColumna(6)
    gestorImagenes.marioMini.salto_derecha = gestorImagenes.marioMini.extraerColumna(5)
    gestorImagenes.marioMini.salto_izquierda = fi_flip(gestorImagenes.marioMini.salto_derecha)
    
    gestorImagenes.marioMini.quieto = comodin()
    gestorImagenes.marioMini.quieto.derecha = gestorImagenes.marioMini.extraerColumna(0)
    gestorImagenes.marioMini.quieto.izquierda = fi_flip(gestorImagenes.marioMini.quieto.derecha)
    
    gestorImagenes.marioMini.caminando_derecha = []
    gestorImagenes.marioMini.caminando_izquierda = []
    for i in range(3):
        img = gestorImagenes.marioMini.extraerColumna(i + 1)
        gestorImagenes.marioMini.caminando_izquierda.append(fi_flip(img))
        gestorImagenes.marioMini.caminando_derecha.append(img)
    gestorImagenes.marioMini.caminando_derecha.append(.1)
    gestorImagenes.marioMini.caminando_izquierda.append(.1)
    
    gestorImagenes.tortuga = gestorImagenes.principal.extraer_usando_tsv("Tortuga", -1, 1.5 * unidad)
    gestorImagenes.tortuga_w = gestorImagenes.tortuga.get_width() / 6
    gestorImagenes.tortuga_h = gestorImagenes.tortuga.get_height()
    gestorImagenes.tortuga_aplastada = gestorImagenes.tortuga.subsurface((
                                                                         4 * gestorImagenes.tortuga_w,
                                                                         0,
                                                                         gestorImagenes.tortuga_w,
                                                                         gestorImagenes.tortuga_h
                                                                         ))
    gestorImagenes.tortuga_caminando_izquierda = []
    gestorImagenes.tortuga_caminando_derecha = []
    for i in range(2):
        img = gestorImagenes.tortuga.subsurface((
                                                i * gestorImagenes.tortuga_w,
                                                0,
                                                gestorImagenes.tortuga_w,
                                                gestorImagenes.tortuga_h
                                                ))
        gestorImagenes.tortuga_caminando_izquierda.append(img)
        gestorImagenes.tortuga_caminando_derecha.append(fi_flip(img))
    gestorImagenes.tortuga_caminando_izquierda.append(.2)
    gestorImagenes.tortuga_caminando_derecha.append(.2)
    
    bowserimg = gestorImagenes.principal.extraer_usando_tsv("Bowser", -1, 2 * unidad)
    bowser_w = bowserimg.get_width() / 4
    bowser_h = bowserimg.get_height()
    gestorImagenes.bowser = []
    for i in range(4):
        gestorImagenes.bowser.append(bowserimg.subsurface((
                                     i * bowser_w, 
                                     0, 
                                     bowser_w, 
                                     bowser_h
                                     )))
    gestorImagenes.bowser.append(1)    
    
    
    gestorImagenes.muffin = gestorImagenes.principal.extraer_usando_tsv("Muffin", -1, unidad)
    gestorImagenes.muffin_w = gestorImagenes.muffin.get_width() / 2
    gestorImagenes.muffin_h = gestorImagenes.muffin.get_height()
    gestorImagenes.muffin_caminando = []
    for i in range(2):
        gestorImagenes.muffin_caminando.append(gestorImagenes.muffin.subsurface((
                                               i * gestorImagenes.muffin_w, 
                                               0, 
                                               gestorImagenes.muffin_w, 
                                               gestorImagenes.muffin_h
                                               )))
    gestorImagenes.muffin_caminando.append(.2)                                       
    gestorImagenes.muffin_aplastado = fi_scale(gestorImagenes.muffin_caminando[0], gestorImagenes.muffin_w, gestorImagenes.muffin_h / 2)
    
    
    gestorImagenes.hongo = gestorImagenes.principal.extraer_usando_tsv("Hongo", -1, unidad)
    gestorImagenes.estrella = gestorImagenes.principal.extraer_usando_tsv("Estrella", -1, unidad)

    
    gestorImagenes.nube1 = gestorImagenes.principal.extraer_usando_tsv("Nube 1", -1, unidad * 1.5)
    gestorImagenes.nube2 = gestorImagenes.principal.extraer_usando_tsv("Nube 2", -1, unidad * 1.5)
    gestorImagenes.nube3 = gestorImagenes.principal.extraer_usando_tsv("Nube 3", -1, unidad * 1.5)
    gestorImagenes.arbusto1 = fi_apagarCanales(gestorImagenes.nube1, .5, .81, .06)
    gestorImagenes.arbusto2 = fi_apagarCanales(gestorImagenes.nube2, .5, .81, .06)
    gestorImagenes.arbusto3 = fi_apagarCanales(gestorImagenes.nube3, .5, .81, .06)
    gestorImagenes.colina2 = gestorImagenes.principal.extraer_usando_tsv("Colina", -1, 2 * unidad)
    gestorImagenes.colina1 = gestorImagenes.colina2.subsurface(
                                                               (0, 0, gestorImagenes.colina2.get_width(), gestorImagenes.colina2.get_height() / 2)
                                                               )
    gestorImagenes.piso = gestorImagenes.principal.extraer_usando_tsv("Piso 1", unidad)
    gestorImagenes.piso1 = gestorImagenes.principal.extraer_usando_tsv("Piso 2", unidad)
    gestorImagenes.cabezaTubo = gestorImagenes.principal.extraer_usando_tsv("Tubo (Cabeza)", -1, unidad)
    gestorImagenes.cuerpoTubo = gestorImagenes.principal.extraer_usando_tsv("Tubo (Cuerpo)", -1, unidad)
    gestorImagenes.ladrillo = gestorImagenes.principal.extraer_usando_tsv("Bloque cabeceable (Ladrillo)", -1, unidad)
    gestorImagenes.cajaMisteriosa = []
    gestorImagenes.cajaMisteriosa.append(
                                         gestorImagenes.principal.extraer_usando_tsv("Bloque cabeceable (Misteriosa)", -1, unidad)
                                         )
    colorBusqueda = 0xFF9B3B
    colorReemplazo = gestorImagenes.cajaMisteriosa[0].get_at((0, 3))
    gestorImagenes.cajaMisteriosa.append(fi_reemplazarCoincidencia(
                                         gestorImagenes.cajaMisteriosa[0], 
                                         colorBusqueda, 
                                         colorReemplazo
                                         ))
    colorReemplazo2 = [int(colorReemplazo[0] * .5), int(colorReemplazo[1] * .5), int(colorReemplazo[2] * .5)]
    gestorImagenes.cajaMisteriosa.append(fi_reemplazarCoincidencia(
                                         gestorImagenes.cajaMisteriosa[0], 
                                         colorBusqueda, 
                                         colorReemplazo2, 
                                         ))
    gestorImagenes.cajaMisteriosa.append(gestorImagenes.cajaMisteriosa[1])
    gestorImagenes.cajaMisteriosa.append(.8 / 4)
    gestorImagenes.cajaUsada = gestorImagenes.principal.extraer_usando_tsv("Bloque cabeceable (Usada)", -1, unidad)
    gestorImagenes.castillo = gestorImagenes.principal.extraer_usando_tsv("Castillo", -1, unidad * 5)
    
def cargarNivel1():
   
    enemigos.append(Tortuga(10, 11.5))
    enemigos.append(Tortuga(107, 11.5))

    enemigos.append(Muffin(22, 12))
    enemigos.append(Muffin(40, 12))
    enemigos.append(Muffin(51, 12))
    enemigos.append(Muffin(52.5, 12))
    enemigos.append(Muffin(80, 4))
    enemigos.append(Muffin(82, 4))
    enemigos.append(Muffin(97, 12))
    enemigos.append(Muffin(98.5, 12))
    enemigos.append(Muffin(114, 12))
    enemigos.append(Muffin(115.5, 12))
    enemigos.append(Muffin(124, 12))
    enemigos.append(Muffin(125.5, 12))
    enemigos.append(Muffin(128, 12))
    enemigos.append(Muffin(129.5, 12))
    
    enemigos.append(Bowser(174, 11))

    
    piso.append(Piso(-1, 0, 1, 15))
    piso.append(Piso(0, 13, 69, 3))
    piso.append(Piso(71, 13, 15, 3))
    piso.append(Piso(89, 13, 64, 3))
    piso.append(Piso(155, 13, 69, 3))
    generarDiagonal_izquierda(134, 9, 4)
    generarDiagonal_derecha(140, 9, 4)
    generarDiagonal_izquierda(148, 9, 4)
    piso.append(Piso(152, 9, 1, 4, gestorImagenes.piso1))
    generarDiagonal_derecha(155, 9, 4)
    generarDiagonal_izquierda(181, 5, 8)
    piso.append(Piso(189, 5, 1, 8, gestorImagenes.piso1))

    
    tubos.append(Tubo(28, 11))
    tubos.append(Tubo(38, 10))
    tubos.append(Tubo(46, 9))
    tubos.append(Tubo(57, 9))
    tubos.append(Tubo(163, 11))
    tubos.append(Tubo(179, 11))

    
    cajas.append(BloqueCabeceable(16, 9, gestorImagenes.cajaMisteriosa))
    cajas.append(BloqueCabeceable(22, 5, gestorImagenes.cajaMisteriosa))
    for i in range(5):
        cajas.append(BloqueCabeceable(20 + i, 9))
    consultarBloqueCabeceable(21, 9).imagen(gestorImagenes.cajaMisteriosa).recompensa(RECOMPENSA_HONGO)
    consultarBloqueCabeceable(23, 9).imagen(gestorImagenes.cajaMisteriosa)
    cajas.append(BloqueCabeceable(64, 8, gestorImagenes.cajaMisteriosa).invisible(true))   
    for i in range(3):
        cajas.append(BloqueCabeceable(77 + i, 9))
    consultarBloqueCabeceable(78, 9).imagen(gestorImagenes.cajaMisteriosa)            
    for i in range(8):
        cajas.append(BloqueCabeceable(80 + i, 5))            
    for i in range(4):
        cajas.append(BloqueCabeceable(91 + i, 5))
    consultarBloqueCabeceable(94, 5).imagen(gestorImagenes.cajaMisteriosa)            
    cajas.append(BloqueCabeceable(94, 9))    
    consultarBloqueCabeceable(94, 9).contadorDeUso(10) 
    for i in range(2):
        cajas.append(BloqueCabeceable(100 + i, 9))
    consultarBloqueCabeceable(101, 9).contadorDeUso(1)
    consultarBloqueCabeceable(101, 9).recompensa(RECOMPENSA_ESTRELLA)
    consultarBloqueCabeceable(101, 9).contadorDeUso(10) 
    for i in range(3):
        cajas.append(BloqueCabeceable(106 + 3 * i, 9))
        consultarBloqueCabeceable(106 + 3 * i, 9).imagen(gestorImagenes.cajaMisteriosa)       
    cajas.append(BloqueCabeceable(109, 5))
    consultarBloqueCabeceable(109, 5).imagen(gestorImagenes.cajaMisteriosa)     
    cajas.append(BloqueCabeceable(118, 9))
    for i in range(3):
        cajas.append(BloqueCabeceable(121 + i, 5))    
    for i in range(4):
        cajas.append(BloqueCabeceable(128 + i, 5))    
    for i in range(2):
        cajas.append(BloqueCabeceable(129 + i, 9))
        consultarBloqueCabeceable(129 + i, 5).imagen(gestorImagenes.cajaMisteriosa)        
    for i in range(4):
        cajas.append(BloqueCabeceable(168 + i, 9))    
    consultarBloqueCabeceable(170, 9).imagen(gestorImagenes.cajaMisteriosa)

    
    patronesDeFondo.append(patronFondo(
                           [
                           elementoDeFondo(0, 11, gestorImagenes.colina2),
                           elementoDeFondo(16, 12, gestorImagenes.colina1), 
                           ], 
                           5, 
                           48))
    patronesDeFondo.append(patronFondo(
                           [
                           elementoDeFondo(11.5, 12, gestorImagenes.arbusto3),
                           elementoDeFondo(23.5, 12, gestorImagenes.arbusto1),
                           elementoDeFondo(41.5, 12, gestorImagenes.arbusto2)
                           ], 
                           5, 
                           48))
    patronesDeFondo.append(patronFondo(
                           [
                           elementoDeFondo(8, 3, gestorImagenes.nube1),
                           elementoDeFondo(19, 2, gestorImagenes.nube1),
                           elementoDeFondo(27, 3, gestorImagenes.nube3),
                           elementoDeFondo(36, 2, gestorImagenes.nube2)
                           ], 
                           5, 
                           48))
    patronesDeFondo.append(patronFondo(
                           [
                           elementoDeFondo(202, 8, gestorImagenes.castillo)
                           ], 
                           1, 
                           0))