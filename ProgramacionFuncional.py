#Funciones de orden superior

def saludar(lengua):
    def saludar_es():
        print("Hola españolito")

    def saludar_gl():
        print("boas")

    def saludar_en():
        print("Hi")

    def saludar_it():
        print("Ciao")

    def saludar_kl():
        print("Nuqneh")

    #definimos que funcion interna lanzara segun la lengua que le pasamos a la funcion superior
    #Fijarse que no ponemos los parentesis, sino ejecutaria las funciones con parentesis nada mas llamar al metodo saludar()
    #antes de llegar al return, independientemente de la lengua que le pasemos
    lengua_funcion = {"es" : saludar_es,"gl" : saludar_gl, "en" : saludar_en, "it" : saludar_it, "kl" : saludar_kl}

    return lengua_funcion[lengua]

#Asignamos a la variable funcion el metodo saludar("es")
funcion = saludar("gl")
#si la imprimimos nos sacaria el __str__ de dicha funcion
print(funcion)
#si llamamos a la variable como si fuese una funcion, ejecutara la funcion que le asignamos
funcion()
#Asi podemos ejecutar directamente el resultado de la funcion interna
saludar("kl")()

#Ejemplo de la funcion map(funcion_a_ejecutar,lista_de_parametros)
def cuadrado(n,m):
    #En el return si usamos comas nos devolvera una tupla con los valores
    #Usando list o corchetes nos devolveria una lista
    return [n**2,m**2]

listaNumeros=[1,2,3,4,5,6,7,8,9,10]
listaNumeros2=[6,7,8]
#Si la funcion tiene mas de un paremetro se le pasarian dos listas al map. En caso de tener diferentes tamaños solo
#ejecutara la funcion mientras haya valores para ambos parametros
l2 = list(map(cuadrado,listaNumeros,listaNumeros2))
print("l2: ",l2)

#Con el metodo filter podemos lograr que una funcion solo nos devuelva los valores que cumplan una condicion
def par(n):
    return (n%2==0)

for i in listaNumeros:
    print(i,"es par? ",par(i))

pares = list(filter(par,listaNumeros))
print("list(filter): ",pares)

#Expresiones lambda:
impares = list(filter(lambda n : n % 2.0 != 0, listaNumeros))
print("list(filter) con lambda",impares)

#Compresion de listas
#en l4 eleva al cuadrado cada elemento n de listaNumeros
l4 =[n**2 for n in listaNumeros]
print("l4: ",l4)

def cubo(n):
    return n**3
#l5 aplica el metodo cubo(n) a cada elemento n de listaNumeros
l5=[cubo(n) for n in listaNumeros]
print("l5: ",l5)

l6 =[n**2 for n in listaNumeros if n % 2 == 0]
print("l6: ",l6)

#Python permite multiplicar cadenas de texto por numeros, en este caso lo haces iterando por
#dos lista con un doble for
l7_1=[0,1,2,3,4,5]
l7_2=["a","b","c"]
l7_3=[s*v
      for s in l7_1
      for v in l7_2
      if s>0]
print("l7: ",l7_3)

#guardamos en la variable l8 la secuencia de generacion que luego usaremos en el for
#a diferencia de l7 no guardamos los resultados en una variable, sino que los generaria a medida que los necesita
#cuando iteramos por ella
l=[1,2,3,4]
l8= (n**2 for n in l)
for i in l8:
    print(i)

#Definir un generador. Esto genera un iterable que tenemos que usar desde un bucle para acceder a cada elemento generado por la funcion
#En este caso lo que nos devuelva el yield
def mi_generador(n,m,s):
    while(n <= m):
        yield n,m*n,s*m
        n+=s

#Usando este tipo de funcion nos permitiria devolver varios valores diferentes, y acceder a ellos como una tupla si iteramos por
#un unico elemento, o a los valores individuales si iteramos por tantos elementos como devuelva el yield
for i,j,k in mi_generador(0,10,4):
    print(i)
    print(k)
    print(j)

for i in mi_generador(0,10,2):
    print(i)


