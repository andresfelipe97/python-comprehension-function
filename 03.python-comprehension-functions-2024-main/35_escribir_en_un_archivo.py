with open('./text.txt', 'w+') as file:                        # 'r+' para poder escribir y leer   #'w+' para leer y reescribir nuevas lienas 
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo\n')                #para escribir en el archivo txt # \n salto de lineas 
    file.write('otra liena\n')
    file.write('otra liena\n')