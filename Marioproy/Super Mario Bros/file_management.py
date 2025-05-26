from graphics import *
import os
import os.path
import urllib.request
import urllib.request as urllib2 

nameFolderFiles = ["Archivos"]

def folderFiles(nombre=null):
    if(nombre is null):
        return nameFolderFiles[0]
    nameFolderFiles[0] = nombre

def generateRoute(name, extension=null):
    createFolder(folderFiles())
    if(extension is null):
        return folderFiles() + "/" + name
    return generateRoute(name + "." + extension.replace(".", ""))

def createFolder(name):
    if(location_exists(name)):
        return
    try:
        os.mkdir(name)
        print("Se ha creado la carpeta: " + name)
    except:
        try:
            os.makedirs(name)
            print("Se ha creado la carpeta: " + name)
        except:
            printErr("No se pudo crear la carpeta: " + name)
        
def location_exists(local):
    try:
        return os.path.exists(local)
    except:
        try:
            return os.path.isfile(local)
        except:
            try:
                import pathlib
                path = pathlib.Path(local)
                path.exists()
            except:
                printErr("ERROR (No se puede verificar la existencia): " + local)
                
def download(url, ubicacion):
    try:
        urllib.request.urlretrieve(url, ubicacion)
        print("Archivo descargado: " + ubicacion + " - de - " + url)
    except:
        printErr("ERROR: (No se pudo descargar): " + str(ubicacion) + "  ---  " + str(url))
        
def saveImage(imagen, ubicacion):
    pygame.image.save(imagen, ubicacion)
    print("imagen guardada: " + ubicacion)
    
def loadImage(local, w=-1, h=-1, url=null):
    if(url != null):
        if(not location_exists(local)):
            download(url, local)
    try:
        img = pygame.image.load(local)
        print("imagen cargada: " + local)
        return fi_scale(img, w, h)
    except:
        printErr("error al cargar: " + local)
        
def matrix_tsv(url, local=null):
    if(local == null):
       
        lines = lines_utf_8_web(url)
    else:
        if(not location_exists(local)):
           
            download(url, local)
        
        lines = lines_utf_8_local(local)
    celdas = []
    for line in lines:
        celdas.append(
                      line
                      .replace("\n", "") 
                      .replace("\r", "") 
                      .split("\t")  
                      )
    print("matriz tsv generada de: " + local)
    return celdas

def lines_utf_8_local(local):
    f = open(local, "r")
    lines = []
    for x in f:
        lines.append(x)
    print("retornando renglones de: " + local)
    return lines

def lines_utf_8_web(url):
    lines = []
    bytesArr = bytes_file_web(url)
    for line in bytesArr:
        lines.append(line.decode("utf-8"))
    print("retornando renglones de: " + url)
    return lines
        
def bytes_file_web(url):
    print("retornando bytes de: " + url)
    return urllib2.urlopen(url)