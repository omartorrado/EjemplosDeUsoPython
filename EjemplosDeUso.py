#Ejemplo de funcion
def func(a,b):
    print(a,"+",b,"=",(a+b))
#Llamada a la funcion anterior
func(2,3)
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
print(g["nombre"],g.keys(),g.values(),g.items(),g.items()[1])
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