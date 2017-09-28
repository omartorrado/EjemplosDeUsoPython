import random,time

atributos = {"fuerza":0,"destreza":0,"resistencia":0,"inteligencia":0,"percepcion":0,"carisma":0}
habilidades ={}


valoresMedios =[]

def generarAtributos():
    charValue = 0
    for x in atributos:
        atributos[x]=random.randrange(1,11)
        charValue+=atributos[x]
        print(x+": "+str(atributos[x]))
    print(atributos)
    print("Character Value: "+str(charValue)+"/60")
    valoresMedios.append(charValue)

def generarHabilidades():
    x="Empty"
    while x!="end":
        x=input("Escribe una habilidad (end para finalizar)")
        if x!="end":
            habilidades[x] = 0
        print(habilidades)


ti = time.time()
for x in range (0,100000001):
    generarAtributos()
tf=time.time()
print("Tiempo: "+str(int(tf-ti))+"s")
valoresMedios.sort()
for x in range (6,61):
    count=0
    for y in valoresMedios:
        if x==y:
            count+=1
    print("Hay "+str(count)+" "+str(x))
#print(valoresMedios)

