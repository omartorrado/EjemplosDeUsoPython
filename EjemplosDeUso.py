#Ejemplo de funcion
def func(a,b):
    print(a,"+",b,"=",(a+b))
#Llamada a la funcion anterior
func(2, 3)
#Llamar a la funcion con los parametros en diferente orden
func(b=5, a=1)
#Definir parametros por defecto, si se le asigna un valor al definir la funcion usara ese valor si no se le pasa el parametro
def func2(a=99,b=0):
    print(a,b)
func2() #imprime 0 0
func2(3) #imprime 3 0
func2(5,10) #imprime 5 10
#Ejemplo de variable
# en python la coma se usa para declarar tuplas: c = 5,4
# para usar numeros flotantes se usa el .
#Tipos de datos en python (no es necesario declarar el tipo, pero podriamos castear como en java con () )
a=  4  #int
#ab = 5l # (o 5L) long, no existe en python 3.5
b = 5.4 #float (se puede usar tb la notacion 4.5e6 y se sigue considerando float)
bb =4.5e66
c = 5 + 4j #complex
d = "string" #str
e = [1,"olamisamira"] #list (es mutable)
f = (2,"adios") #tuple (es inmutable)
g = {"nombre":"Paco","numero":45.5} #dict (es mutable)
h = False #bool (si convertimos a int un booleano 1=True, 0=False
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))
print(a, b, c, d, e[0], f[1], g, g["nombre"], g["numero"], h)
#Para forzar un tipo de dato se usa el nombre de tipo seguido del valor entre parentesis
# si la conversion no es posible dara error
print(int(e[0]), float(a), complex(b), str(g),)
#Operadores: +,-,*,/,**(elevado a),//(division entera),%(modulo)
#Operadores booleanos: and/or/not
print(True and False)
print(True or False)
print(not True)
#para castear de un tipo a otro se usan funciones propias de cada clase
print("Combinamos una string con un numero casteado a str:"+"hola"+str(5))
print("En la siguiente linea sumamos un 5 con un 4 tipo string casteado a int")
print(5+int("4"))
#En las listas y tuplas se empieza a contar desde el 0.
#Si contamos en negativos el -1 es el ultimo, -2 el antepenultimo, etc
#Este metodo no sirve para los dics pq no estan ordenados, a estos se accede con el nombre de la key
print(g["nombre"],g.keys(),g.values(),g.items())
#Con .title() obtenemos el nombre de la clave (con la primera letra en mayuscula)
#El .lower() pone la str en minusculas
for x in g:
    g[x.title().lower()]=666
    print(g)
#Para anhadir elementos a una list usamos .append(dato que queremos anhadir)
e.append(45)
print(e)
#si queremos acceder a parte de un elemento se haria como a continuacion (inicio:fin:salto/:fin/::salto)
print(e[1][::3])
#Para quitarlos usamos .pop() e indicamos la posicion a borrar (en caso de no indicarla borrara el ultimo elemento)
e.pop(1)
print(e)
#Controles de flujo
numero=5
numero2 =9
tupla=(1,2,3,4,5)
#Bucle if-elif(else if)-else
if numero<5:
    print("Menor de 5")
elif numero>5:
    print("Mayor de 5")
else:
    print("es un 5")
#Bucle for para iterar una coleccion
for x in tupla:
    print(x)
#Bucle for para un rango de numeros, el primero es inclusivo y el ultimo exclusivo (para 1-10 usaremos 1-11)
for x in range (2,10):
    print(x)
#Bucle while
while numero<10:
    print("numero"+str(numero))
    numero += 1
#Clases
class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def mostraX(self):
        print ("Coordenada x: "+str(self.x))
#herencia circulo hereda de punto
class Circulo(Punto):
    def __init__(self,x,y,r):
        Punto.__init__(self,x,y)
        self.r = r
    def metodoRepetido(self):
        print("Soy circulo")
c1=Circulo(3,5,3)
c1.mostraX();
#herencia multiple. cilindro hereda tanto de circulo como de terceradimension
#En caso de que compartan metodos con el mismo nombre las clases de las que heredamos
#se quedaria con el metodo de la primera que le pasamos como parametro, en este ejemplo
#con el metodo metodoRepetido de Circulo
class TerceraDimension:
    def __init__(self,h):
        self.h = h
    def mostraH(self):
        print("Altura: "+str(self.h))
    def metodoRepetido(self):
        print("Soy tercera dimension")

import math
class Cilindro(Circulo,TerceraDimension):
    def __init__(self,x,y,r,h):
        Circulo.__init__(self,x,y,r)
        TerceraDimension.__init__(self,h)
    def volumen(self):
        return math.pi*self.r**2*self.h
    #los metodos o variables definidos con _ antes del nombre se consideran privados
    # no los podemos llamar desde fuera de la propia clase
    def _superficie(self):
        print(self.h)
        return 2*math.pi*self.r**2+2*math.pi*self.r*self.h
    def verSuperficie(self):
        print(self._superficie())

c2= Cilindro(1,1,1,1)
print(c2.volumen())
c2.metodoRepetido()
c2.verSuperficie()
#Diccionarios
dict={100:"Miguel",101:"Adrian",102:"Silva"}
#para acceder a los datos tenemos dos maneras
print(dict[100])
print(dict.get(100))
#Si le pedimos una clave que no existe nos devolverá none, pero podemos evitar esto pasandole un valor por defecto
print(dict.get(103))
print(dict.get(103,"Clave no encontrada"))
#el metodo contains nos devuelve true o false si la key esta en el diccionario
print(dict.__contains__(103))
#Hay varios metodos con los que podemos acceder a diferente informacion del diccionario
print("Items:",dict.items())
print("Values:",dict.values())
print("Keys:",dict.keys())
print("Size of:",dict.__sizeof__())
#los metodos .items(), .values() y .keys() devuelven una vista del diccionario (dictview), si queremos acceder a un elemento
#concreto hay que castearlas como una lista
print(list(dict.keys())[2])
#Podemos iterar un diccionario a traves de su lista de items para acceder a los pares clave-valor (los podriamos llamar
#como queramos al crear el bucle)
for clave,valor in dict.items():
    print("clave:"+str(clave)+", valor:"+str(valor))
#Tb lo podriamos hacer con las keys o los values
for key in dict.keys():
    print("Clave:"+str(key))
for value in dict.values():
    print("Valor:"+str(value))
#Con el metodo len() podemos averiguar la cantidad de elementos de un diccionario, o de una dictview
print(len(dict))
#con pop eliminamos una key del diccionario y nos devuelve el valor, que podriamos guardar en una variable
valor=dict.pop(100)
print("Aqui vemos como queda el dict tras hacer pop(100): "+str(dict.items()),"Este es el valor guardado en la variable: "+valor)
#Funciones default
cadena ="Hola, soy una string, hola"
print("string Split: "+str(cadena.split(" ")))
print("string Count(ol): "+str(cadena.count("ol")))
print(cadena)
#Funciones de listas
lista=[12,"soy una lista",(7,7),{1:"Miguel",2:"Paco"},12,12]
print(lista)
print("Lista count(): "+str(lista.count(12)))