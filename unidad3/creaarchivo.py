
archivo = open("archivo1.txt", "w")
archivo.write("a\n")
archivo.write("b\n")
archivo.write("c\n")
archivo.close()
print("Archivo1.txt creado correctamente")

archivo = open("archivo2.txt", "w")
archivo.write("a\n")
archivo.write("a\n")
archivo.write("c\n")
archivo.close()
print("Archivo2.txt creado correctamente")