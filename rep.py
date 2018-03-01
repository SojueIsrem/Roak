from os import listdir
from os.path import isfile, join

from pygame import mixer
from os import listdir

def ls(ruta):
    return listdir(ruta)

lista = ls('/home/soju3/Documentos/py/RO/musica/')
e =0
for i in lista:
    e+=1
    print(e,": ",i)
num = input("Numero de rola ")
#print()
track = int(num)-1
file = '/home/soju3/Documentos/py/RO/musica/'+lista[track]
print(lista[track])
mixer.init()
mixer.music.load(file)
mixer.music.play()
