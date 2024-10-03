#!/bin/bash
gmt begin test_map png
  gmt basemap -R-180/180/-90/90 -JX15c/10c -Baf -BWSen
  gmt coast -Wthin -Df -N1/0.5p,black
gmt end show
