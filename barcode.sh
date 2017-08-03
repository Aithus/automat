barcode -b "$1" -o "/tmp/barcode.eps" -u "mm" -e code128 -p 60x5 -g 70x10+0+0 -E -n 
convert -density 100 /tmp/barcode.eps -flatten /tmp/barcode.png
