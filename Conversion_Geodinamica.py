# -*- coding: utf-8 -*-
"""
CONVERSIÓN GEODINÁMICA
"""

import numpy as np
import math



#fUNCIONES
def miliarcs_rad(wxi,wyi,wzi):
    wx=wxi*(1/4.84814e-9)*(10**6) #grad/Ma
    wy=wyi*(1/4.84814e-9)*(10**6) #grad/Ma
    wz=wzi*(1/4.84814e-9)*(10**6) #grad/Ma
    return wx,wy,wz

def miliarcs_grad(wxi,wyi,wzi):
    wx=wxi*(1/3600000)*(10**6) #grad/Ma
    wy=wyi*(1/3600000)*(10**6) #grad/Ma
    wz=wzi*(1/3600000)*(10**6) #grad/Ma
    return wx,wy,wz

#Convertir coordenadas (wx,xy,wz) a (Lat,Lon,VelAngular)
def convertirCoord(wx,wy,wz):
    
    Lat=np.arctan(wz/(np.sqrt(wx**2+wy**2)))

    Lon=np.arctan(wy/wx)

    w=np.sqrt(wx**2+wy**2+wz**2)

    return Lat,Lon,w

#Prueba:
#Convertir unidades miliarcs por segundo a grados
wxi=-0.19
wyi=-0.442
wzi=0.915

wx,wy,wz=miliarcs_grad(wxi,wyi,wzi)

Lat,Lon,w=convertirCoord(wx,wy,wz)
#print(math.degrees(Lat))
#print(math.degrees(Lon))
#print(math.degrees(w))

#Nazca:
wxN=-0.33
wyN=-1.551
wzN=1.625

#Pacifico:
wxP=-0.411
wyP=1.036
wzP=-2.166

#Obtener Movimiento relativo Nazca respecto pacífico:
PwxN=wxN+wxP
PwyN=wyP-wyN
PwzN=wzN-wzP

#print(PwxN)
#print(PwyN)
#print(PwzN)

wx,wy,wz=miliarcs_grad(PwxN,PwyN,PwzN)
Lat,Lon,w=convertirCoord(wx,wy,wz)

print(math.degrees(Lat))
print(math.degrees(Lon))
print(w)