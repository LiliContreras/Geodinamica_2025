#!/bin/bash

# Archivo de salida
output=mapa_VGPs_E2_Nuevo

data=VGPs_E2.txt

# Empiezo a hacer el mapa:
gmt begin $output png
	#gmt coast -Rg -JQ0/12c -B60f30g30 -Dc -A5000 -Gtan4 -Slightcyan --GMT_THEME=cookbook
	#->gmt coast -Rg -JE-100/40/12c -Bg -Dc -A10000 -Glightgray -Wthinnest --GMT_THEME=cookbook 
	#gmt coast -R0/360/-80/80 -JT330/-45/10c -Ba30g -BWSne -Dc -A2000 -Slightblue -G0 --MAP_ANNOT_OBLIQUE=lon_horizontal --GMT_THEME=cookbook
	gmt coast -Rd -JR12c -Bg -Dc -A10000 -Gburlywood4 -Swheat1 --GMT_THEME=cookbook
	#gmt coast -Rg -JQ12c -B60f30g30 -Dc -A5000 -Gtan4 -Slightcyan --GMT_THEME=cookbook
    	gmt plot $data -Sc0.1c -Gred -Wthin,black  # Agregar los puntos en el mapa

gmt end show
