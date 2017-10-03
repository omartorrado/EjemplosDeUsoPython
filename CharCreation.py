import random, time

atributos = {"fuerza": 0, "destreza": 0, "resistencia": 0, "inteligencia": 0, "percepcion": 0, "carisma": 0}
habilidades = {}

tiradas1 = 0
tiradas2 = 0
tiradas3 = 0
tiradas4 = 0
tiradas5 = 0
tiradas6 = 0
tiradas7 = 0
tiradas8 = 0
tiradas9 = 0
tiradas10 = 0

valoresMedios = []


def generarAtributos():
    charValue = 0
    for x in atributos:
        atributos[x] = random.randrange(1, 11)
        charValue += atributos[x]
        print(x + ": " + str(atributos[x]))
        # guardamos el numero de tiradas de cada valor
        if atributos[x] == 1:
            global tiradas1
            tiradas1 += 1
        elif atributos[x]==2:
            global tiradas2
            tiradas2 += 1
        elif atributos[x]==3:
            global tiradas3
            tiradas3 += 1
        elif atributos[x]==4:
            global tiradas4
            tiradas4 += 1
        elif atributos[x]==5:
            global tiradas5
            tiradas5 += 1
        elif atributos[x]==6:
            global tiradas6
            tiradas6 += 1
        elif atributos[x]==7:
            global tiradas7
            tiradas7 += 1
        elif atributos[x]==8:
            global tiradas8
            tiradas8 += 1
        elif atributos[x]==9:
            global tiradas9
            tiradas9 += 1
        elif atributos[x]==10:
            global tiradas10
            tiradas10 += 1
        else:
            print("error")
    print(atributos)
    print("Character Value: " + str(charValue) + "/60")
    valoresMedios.append(charValue)


def generarHabilidades():
    x = "Empty"
    while x != "end":
        x = input("Escribe una habilidad (end para finalizar)")
        if x != "end":
            habilidades[x] = 0
        print(habilidades)


ti = time.time()
for x in range(0, 10000):
    generarAtributos()

tf = time.time()
print("Tiempo: " + str(int(tf - ti)) + "s")
valoresMedios.sort()
for x in range(6, 61):
    count = 0
    for y in valoresMedios:
        if x == y:
            count += 1
    print("Hay " + str(count) + " " + str(x))
print("Hay "+str(tiradas1)+" unos")
print("Hay "+str(tiradas2)+" doses")
print("Hay "+str(tiradas3)+" treses")
print("Hay "+str(tiradas4)+" cuatros")
print("Hay "+str(tiradas5)+" cincos")
print("Hay "+str(tiradas6)+" seises")
print("Hay "+str(tiradas7)+" sietes")
print("Hay "+str(tiradas8)+" ochos")
print("Hay "+str(tiradas9)+" nueves")
print("Hay "+str(tiradas10)+" dieces")
print("Se han realizado "+str((tiradas1+tiradas2+tiradas3+tiradas4+tiradas5+tiradas6+tiradas7+tiradas8+tiradas9+tiradas10))+" tiradas")
# print(valoresMedios)
