archivo1 = open("archivo1.txt", "r")
archivo2 = open("archivo2.txt", "r")

lineas1 = archivo1.readlines()
lineas2 = archivo2.readlines()
archivo1.close()
archivo2.close()


print(lineas1)
print(lineas2)

print("Voy a comparar linea por linea los 2 archivos")
print("1: Son iguales, 0: No es igual")

for i in range(len(lineas1)):
    respuesta1 = lineas1[i].strip()
    respuesta2 = lineas2[i].strip()

    if respuesta1 == respuesta2:
        print(1)
    else:
        print(0)
