#Punto 6 al 11

from io import open
import collections
import string
import re
from matplotlib import pyplot as plt
# punto 6

Quijote = open("DonQuijote.txt", mode="r", encoding="utf-8")
text = Quijote.read()
print((text), '\n')
# punto 7
lineas=text.splitlines()
print("7) Cantidad de lineas:", len(lineas), "\n")
 
text = re.sub("\n", "", text)

palabras = text.split(" ")
diccionario = dict()

print("8) Palabras que aparecen - Cantidad de veces:","\n")

for p in palabras:
    diccionario[p] = diccionario.get(p, 0) + 1

print(diccionario)

print("\n")
print("9) Palabras con mas Frecuencia")

p=0;
x = []
y = []

counter = collections.Counter(text.split())
for word, cont in counter.most_common():
        if p<5:
            print(f"'{word}' se muestra {cont} {'veces' if cont > 1 else 'vez'}.")
            p=p+1
            x.append(word)
            y.append(cont)
        else:
            print("\n")
            
            break;
print("10) Conjunto de datos")
print(x)
print(y)

plt.bar(x, y, color ='gray') 
plt.title('Grafica Words vs Time it repeat') 
plt.ylabel('# of times') 
plt.xlabel('Words')  

plt.show()