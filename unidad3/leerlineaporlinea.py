# Este programa abre un archivo y lo lee 
# línea por línea

# Paso 1. Leer el archivo
archivo = open("archivo2.txt", "r")

for linea in archivo:
    print(linea.strip())

archivo.close()
