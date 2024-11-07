#!/bin/bash

# Archivo de salida
output=mapa_puntos_otravista

data=puntos_gmt_nuevos.txt

# Empiezo a hacer el mapa:
gmt begin $output png
	#gmt coast -Rg -JQ0/12c -B60f30g30 -Dc -A5000 -Gtan4 -Slightcyan --GMT_THEME=cookbook
	gmt coast -Rg -JE-100/40/12c -Bg -Dc -A10000 -Glightgray -Wthinnest --GMT_THEME=cookbook 
	#gmt coast -Rg -JQ12c -B60f30g30 -Dc -A5000 -Gtan4 -Slightcyan --GMT_THEME=cookbook
    	gmt plot $data -Sc0.1c -Gred -Wthin,black  # Agregar los puntos en el mapa

gmt end show
