from graphics import *

transformGraphics = [null]

def transform(transf=null):
    if (transformGraphics[0] == null):
        transformGraphics[0] = Transform()
    if(transf is null):
        return transformGraphics[0]
    transformGraphics[0] = transf

def transformPoint(point, tx=null, ty=null, sx=null, sy=null, theta=null):
    return transform().transformPoint(point, tx, ty, sx, sy, theta)

def transformPoint_int(point, tx=null, ty=null, sx=null, sy=null, theta=null):
    return toPoint_int(transformPoint(point, tx, ty, sx, sy, theta))

def transformInversePoint(point, tx=null, ty=null, sx=null, sy=null, theta=null):
    return transform().transformInversePoint(point, tx, ty, sx, sy, theta)

def translate(point=null):
    if(point is not null):
        transform().setTranslate(point)
    else:
        return transform().getTranslate()

def translateX(x=null):
    if(x is not null):
        transform().setTranslateX(x)
    else:
        return transform().getTranslateX()

def translateY(y=null):
    if(y is not null):
        transform().setTranslateY(x)
    else:
        return transform().getTranslateY()

def getInvertY():
    return transform().getInvertY()

def setInvertY(bool):
    transform().setInvertY(bool)

def setScale(e):
    transform().setScale(e)

def setScaleY(e):
    transform().setScaleY(e)

def setScaleX(e):
    transform().setScaleX(e)

def getScale():
    return transform().getScale()

def getScaleA():
    e = transform().getScale()
    return (e[0] + e[1]) / 2

def getScaleX():
    return transform().getScaleX()

def getScaleY():
    return transform().getScaleY()

def theta(t=null):
    if(t is null):
        transform().setTheta(t)
    else:
        return transform().getTheta()


#-----------CLASS

class Transform:
    
    translate = [0, 0]
    scale = [1, 1]
    invertY = [False]
    theta = [0]

    def setTranslate(self, point):
        self.translate[0] = point[0]
        self.translate[1] = point[1]

    def setTranslateX(self, x):
        self.translate[0] = x

    def setTranslateY(self, y):
        self.translate[1] = y

    def getTranslate(self):
        return self.translate

    def getTranslateX(self):
        return self.translate[0]

    def getTranslateY(self):
        return self.translate[1]

    def getInvertY(self):
        return self.invertY[0]

    def setInvertY(self, bool):
        self.invertY[0] = bool

    def setScale(self, e):
        self.scale[0] = e
        self.scale[1] = e

    def setScaleY(self, e):
        self.scale[1] = e

    def setScaleX(self, e):
        self.scale[0] = e

    def getScale(self):
        return self.scale

    def getScaleX(self):
        return self.scale[0]

    def getScaleY(self):
        return self.scale[1]

    def getTheta(self):
        return self.theta[0]

    def setTheta(self, t):
        self.theta[0] = t

    def resetTransform(self):
        self.setTranslate([0, 0])
        self.setScale(1)
        self.setTheta(0)

    def transformPoint(self, point, tx=null, ty=null, sx=null, sy=null, theta=null):
        if(tx is null):
            tx = self.getTranslateX()
        if(ty is null):
            ty = self.getTranslateY()
        if(sx is null):
            sx = self.getScaleX()
        if(sy is null):
            sy = self.getScaleY()
        if(theta is null):
            theta = self.getTheta()
        retorno = point
        retorno = self.rotatePoint(retorno, theta)
        retorno = self.scalePoint(retorno, sx, sy)
        retorno = self.translatePoint(retorno, tx, ty)
        return retorno

    def transformPoint_int(self, point, tx=null, ty=null, sx=null, sy=null, theta=null):
        return toPoint_int(self.transformPoint(point, tx, ty, sx, sy, theta))

    def transformInversePoint(self, point, tx=null, ty=null, sx=null, sy=null, theta=null):
        if(tx is null):
            tx = self.getTranslateX()
        if(ty is null):
            ty = self.getTranslateY()
        if(sx is null):
            sx = self.getScaleX()
        if(sy is null):
            sy = self.getScaleY()
        if(theta is null):
            theta = self.getTheta()
        retorno = point
        retorno = self.translateInversePoint(retorno, tx, ty)
        retorno = self.scaleInversePoint(retorno, sx, sy)
        retorno = self.rotateInversePoint(retorno, theta)
        return retorno

    def transformInversePoint_int(self, point, tx=null, ty=null, sx=null, sy=null, theta=null):
        if(tx is null):
            tx = self.getTranslateX()
        if(ty is null):
            ty = self.getTranslateY()
        if(sx is null):
            sx = self.getScaleX()
        if(sy is null):
            sy = self.getScaleY()
        if(theta is null):
            theta = self.getTheta()
        return toPoint_int(self.transformInversePoint(point, tx, ty, sx, sy, theta))

    def rotatePoint(self, point, theta=null):
        if(theta is null):
            theta = self.getTheta()
        a = math.cos(theta)
        b = math.sin(theta)
        X = point[0]
        Y = point[1]
        return [a * X - b * Y, b * X + a * Y]

    def rotatePointFixed(self, point, pointFixed=[0, 0], theta=null):
        puntoTemporal = self.translatePoint(point, -pointFixed[0], -pointFixed[1])
        puntoTemporal = self.rotatePoint(puntoTemporal, theta)
        puntoTemporal = self.translatePoint(puntoTemporal, pointFixed[0], pointFixed[1])
        return puntoTemporal

    def rotatePointsPointFixed(self, points, pointFixed=[0, 0], theta=null):
        retorno = []
        for punto in points:
            retorno.append(self.rotatePointFixed(punto, pointFixed, theta))
        return retorno

    def rotatePoints(self, points, theta=null):
        retorno = []
        for punto in points:
            retorno.append(self.rotatePoint(punto, theta))
        return retorno

    def rotateInversePoint(self, point, theta=null):
        if(theta is null):
            theta = self.getTheta()
        a = math.cos(-theta)
        b = math.sin(-theta)
        X = point[0]
        Y = point[1]
        return [a * X - b * Y, b * X + a * Y]

    def scalePoint(self, point, sx=null, sy=null):
        if(sx is null):
            sx = self.getScaleX()
        if(sy is null):
            if(sx is not null):
                sy = sx
            else:
                sy = self.getScaleY()
        iY = 1
        if(self.getInvertY()):
            iY = -1
        return [point[0] * sx, iY * point[1] * sy]

    def scalePointFixed(self, point, pointFixed=[0, 0], sx=null, sy=null):
        puntoTemporal = self.translatePoint(point, -pointFixed[0], -pointFixed[1])
        puntoTemporal = self.scalePoint(puntoTemporal, sx, sy)
        puntoTemporal = self.translatePoint(puntoTemporal, pointFixed[0], pointFixed[1])
        return puntoTemporal

    def scalePointsPointFixed(self, points, pointFixed=[0, 0], sx=null, sy=null):
        retorno = []
        for punto in points:
            retorno.append(self.scalePointFixed(punto, pointFixed, sx, sy))
        return retorno

    def scaleInversePoint(self, point, sx=null, sy=null):
        if(sx is null):
            sx = self.getScaleX()
        if(sy is null):
            if(sx is not null):
                sy = sx
            else:
                sy = self.getScaleY()
        iY = 1
        if(self.getInvertY()):
            iY = -1
        return [point[0] / sx, iY * point[1] / sy]

    def translatePoint(self, point, tx=null, ty=null):
        if(tx is null):
            tx = self.getTranslateX()
        if(ty is null):
            ty = self.getTranslateY()
        return [point[0] + tx, point[1] + ty]

    def translatePoints(self, puntos, trasladarX=null, trasladarY=null):
        retorno = []
        for punto in puntos:
            retorno.append(self.translatePoint(punto, trasladarX, trasladarY))
        return retorno

    def translateInversePoint(self, point, tx=null, ty=null):
        if(tx is null):
            tx = self.getTranslateX()
        if(ty is null):
            ty = self.getTranslateY()
        return [point[0] - tx, point[1] - ty]