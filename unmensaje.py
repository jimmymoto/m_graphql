def readFile(pathFile):
    with open(pathFile, 'r') as file:
        for line in file:
            name, val = line.split('=')
            return val.replace('\n', '') if name == 'registro' else ''

def messageOut(option, fileproperties):
    if 'archivo' in readFile(fileproperties):
        outF = open("archivosalida.txt", "w")
        outF.write(option)
        outF.close()
    else:
        print(option)    

filename = 'registrador.properties'        
option = str(input("Ingrese un mensaje:")) 
messageOut(option, filename)
