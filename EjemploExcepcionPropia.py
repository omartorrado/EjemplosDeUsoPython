#Entre parentesis heredamos de la clase Exception
class MiExcepcion (Exception):

    #Definimos el constructor de la clase
    def __init__(self,valor):
        self.valor = valor

    def __str__(self):
        return "Error: " + str(self.valor)


n=15

try:
    if n == 15:
        raise MiExcepcion("Mi Excepcion")
except MiExcepcion as e:
    print(e)

