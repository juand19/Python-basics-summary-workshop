#En este codigo se busca hacer un bucle de un diccionario
#primero definimos una función main que al final se declara como principal con el IF
#Aunque el def no permite ejecutar el archivo .py correctamente, por lo que se comenta

#def main():
#A continuación se realiza una serie de datos en el “stock” donde tenemos una secuencia de títulos y valores  
stocks = {														#Se crea un dictado que contiene codigo y valores
'IBM': 146.48,
'MSFT': 44.11,
'CSCO': 25.54
}
#print out all the keys
# Se recorre el c para imprimir los datos puestos anteriormente
for c in stocks:
    print(c)

 #print key n values
#El siguiente es para repetir cada clave y valor del “stock” con un formato que tenga Code y la otra fila Value
for k, v in stocks.items():
    print("Code : {0}, Value : {1}".format(k, v))

#En el siguiente If declaramos el main como funcion principal
#Pero se comenta al causar error en el codigo y al no ser necesario

#if __name__ == '__main__':
# main()
