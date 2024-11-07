#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:02:21 2024

@author: lili
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
plt.close('all')

#Puntos: Prueba1
'''
points = np.array([
    [-90.0, -45.65],
    [-68.60, 160.33],
    [-59.55, 146.59],
    [-52.48, -172.30],
    [-46.40, 2.46],
    [-40.93, -109.70],
    [-35.89, 109.46],
    [-31.15, -72.68],
    [-26.63, 45.68],
    [-22.29, 172.29],
    [-18.08, -23.96],
    [-13.97, -148.15],
    [-9.93, 167.10],
    [-5.94, 108.15],
    [-1.98, 101.35],
    [1.98, -101.30],
    [5.94, 84.66],
    [9.93, 82.18],
    [13.97, -121.69],
    [18.08, 42.12],
    [22.29, 88.79],
    [26.63, -62.83],
    [31.15, 117.40],
    [35.89, 78.96],
    [40.93, -177.08],
    [46.40, -52.68],
    [52.48, 27.63],
    [59.55, 5.89],
    [68.60, 172.00],
    [90.0, -23.03]
])
'''
num_points = 30

# Latitudes
#latitudes = np.linspace(-87.5, 87.5, num_points)

# Longitudes
#longitudes = np.random.uniform(-180, 180, num_points)

# puntos:
#points = list(zip(latitudes, longitudes))
#points = [(round(lat, 3), round(lon, 3)) for lat, lon in zip(latitudes, longitudes)]


#random_points
#df = pd.DataFrame(points, columns=['Latitud', 'Longitud'])

#df.to_csv('/home/lili/Documents/Maestria/Geodinamica_2025/Points_VGP_GMT/puntos_gmt_nuevos.txt', sep=' ', index=False, header=False)

directorio = '/home/lili/Documents/Maestria/Geodinamica_2025/Points_VGP_GMT/'
archivo = "puntos_gmt_nuevos.txt"
file = directorio + archivo
df = pd.read_csv(file,sep=' ',header=None)

#Inclinación:
inclinaciones=[-70.219,	-66.438,-65.166,-61.783,-59.580,-58.145,-54.197,-71.836,-63.673,-61.335,-58.900,-54.636,-34.350,-27.158,-7.789,19.743,-6.903,9.247,43.080,34.275,60.575,60.130,62.361,74.406,75.302,74.644,80.505,85.079,87.288,89.430]

#Declinacion: por si las dudas
declinaciones=[	-5.327,-27.784,31.348,28.380,-40.175,-33.392,27.329,23.684,-45.199,16.641,-27.862,-24.111,12.239,10.349,10.123,-13.395,-8.602,1.059,10.342,-4.904,-8.466,-1.021,5.584,-12.279,-12.146,-2.214,26.456,-21.022,5.061,-173.106]

#Graficar curva I=f(L)
I=np.atan(2*np.tan(df[0]))

plt.plot(df[0],I)
plt.xlabel('Latitud')
plt.ylabel('Inclinación')
plt.show()

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
        lon_vgp_rad=lon_rad+np.pi-beta
        lon_vgp_deg = math.degrees(lon_vgp_rad)
    return lon_vgp_deg

#Lista para almacenar Latitudes
Lats=[]
#Lista para almacenar Longitudes
Longs=[]

for i in range(len(inclinaciones)):
    P,latp_rad,latp_deg,beta=latitud_vgp(df[0][i], df[1][i], declinaciones[i], inclinaciones[i])
    lon_vgp_deg=longitud_vgp(P, df[0][i], latp_rad, beta, df[1][i])
    Lats.append(latp_deg)
    Longs.append(lon_vgp_deg)
    
df_VGPs = pd.DataFrame(list(zip(Lats, Longs)),columns =['Latitud', 'Longitud'])
df_VGPs.to_csv('/home/lili/Documents/Maestria/Geodinamica_2025/Points_VGP_GMT/VGPs_E2.txt', sep=' ', index=False, header=False)
