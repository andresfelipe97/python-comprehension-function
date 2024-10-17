file = open('./text.txt')        #para abir el archivo 
#print(file.read())              #para leer el archivo completo 

print(file.readline())           #para leer linea a linea del archivo
print(file.readline())           #para leer linea a linea del archivo

for line in file:                #leer linea a linea iterando en las lineas del archivo
    print(line)

file.close()                     #cerrar el archivo 

with open('./text.txt') as file:       #abre el archivo y lo lee linea a linea sin preocupacion de estar cerrando el archivo
    for line in file:
        print(line)