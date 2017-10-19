import random

def tiradaVariosDados(dados,caras):
    resultados=[]
    for x in range (1,dados+1):
        resultados[x]=random.randrange(1,caras+1)
    return resultados

def tiradaMediaDados(dados,caras):
    resultados=0
    for x in range(1,dados+1):
        numero=random.randrange(1,caras+1)
        print("tirada:",numero)
        resultados+=numero
        print("Total "+str(resultados))
    print("Media truncada "+str(int(resultados/dados)))
    print("Modulo "+str(resultados%dados))
    #el modulo no es lo que me interesa, sino comprobar el valor del resto en la division
    return round(resultados/dados)

tiradaMediaDados(3,10)