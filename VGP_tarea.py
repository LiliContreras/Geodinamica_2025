#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:46:41 2024

@author: lili

#VIRTUAL GEOMAGNETIC POLE
#Geodinamica
#Tarea
"""

import numpy as np
import math

#FUNCION CALCULO LATITUD
def latitud_vgp(lat,lon,D,I):
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    I_rad = math.radians(I)
    D_rad = math.radians(D)
    #Colatitud:
    P=math.atan(2/(math.tan(I_rad)))
    #Latitud del polo:
    lat_VGP_rad = math.asin(math.sin(lat_rad) * math.cos(P) + 
                    math.cos(lat_rad) * math.sin(P) * math.cos(D_rad))
    lat_vgp_deg = math.degrees(lat_VGP_rad)
    #Beta:
    beta=math.asin(math.sin(P)*math.sin(D_rad)/math.cos(lat_VGP_rad))
    return P,lat_VGP_rad,lat_vgp_deg,beta

def longitud_vgp(P,lat,lat_vgp,beta,lon):
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)  
    #Longitud:
    if math.cos(P)>=math.sin(lat_rad)*math.sin(lat_vgp):
        #print(math.cos(P))
        a=math.sin(lat_rad)*math.sin(lat_vgp)
        #print(a)
        print('caso 1')
        lon_vgp_rad=lon_rad+beta
        lon_vgp_deg = math.degrees(lon_vgp_rad)
    else:
        print('caso 2')
        lon_vgp_rad=lon_rad+180-beta
        lon_vgp_deg = math.degrees(lon_vgp_rad)
    return lon_vgp_deg

#Lista para almacenar Latitudes
Lats=[]
#Lista para almacenar Longitudes
Longs=[]

#Sitio A:
lat_muestra = -20 #S; 
lon_muestra = -65 #W
D = 0 
I = 0.01

P,latp_rad,latp_deg,beta=latitud_vgp(lat_muestra, lon_muestra, D, I)
lon_vgp_deg=longitud_vgp(P, lat_muestra, latp_rad, beta, lon_muestra)
Lats.append(latp_deg)
Longs.append(lon_vgp_deg)
#Faltan elipses error:

#Sitio B
lat_muestra = -20.0 #S; 
lon_muestra = 30.0 #E; 
D = 0.0 
I = 0.01

P,latp_rad,latp_deg,beta=latitud_vgp(lat_muestra, lon_muestra, D, I)
lon_vgp_deg=longitud_vgp(P, lat_muestra, latp_rad, beta, lon_muestra)
Lats.append(latp_deg)
Longs.append(lon_vgp_deg)

#Sitio C
lat_muestra = 0.0#(ecuador); 
lon_muestra = 30.0 #E; 
D = 50 #(N 50 E);
I = 0.01

P,latp_rad,latp_deg,beta=latitud_vgp(lat_muestra, lon_muestra, D, I)
lon_vgp_deg=longitud_vgp(P, lat_muestra, latp_rad, beta, lon_muestra)
Lats.append(latp_deg)
Longs.append(lon_vgp_deg)

#Sitio D
lat_muestra = 0.0#(ecuador); 
lon_muestra = 30.0#E; 
D = 50 #(N 50 E);
I = -90 #(el vector magnético esta apuntando hacia arriba)

P,latp_rad,latp_deg,beta=latitud_vgp(lat_muestra, lon_muestra, D, I)
lon_vgp_deg=longitud_vgp(P, lat_muestra, latp_rad, beta, lon_muestra)
Lats.append(latp_deg)
Longs.append(lon_vgp_deg)

# Convertir de radianes a grados para la latitud del VGP






