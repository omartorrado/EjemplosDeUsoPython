import gi
import time
gi.require_version("Gtk",'3.0')
from gi.repository import Gtk

class MainWindow:

    def __init__(self):
        ruta= "/home/local/DANIELCASTELAO/otorradomiguez/PycharmProjects/EjemplosDeUso/UsandoGlade.glade"
        builder = Gtk.Builder()
        builder.add_from_file(ruta)
        self.ventana=builder.get_object("ventana1")
        #Comentamos la siguiente linea pq ya indicamos
        #self.ventana.show_all()
        self.txtSaudo=builder.get_object("txtSaudo")
        self.labelSaudo=builder.get_object("labelSaudo")
        self.boton1=builder.get_object()
        #señales(eventos)
        eventos={"MainWindow_Destroy":Gtk.main_quit,"boton1Clicked":self.boton1Clicked,"boton2Clicked":self.boton2Clicked}
        builder.connect_signals(eventos)

    #Gtk button devuelve un argumento indicando el boton usado (o su posicion en memoria)
    def boton1Clicked(self,event):
        #print(event)
        print("Hola")
        self.labelSaudo.set_text(self.txtSaudo.get_text()+" Bienvenido")
        self.txtSaudo.set_text("")

    def boton2Clicked(self,event):
        #print(event)
        print("No hago nada")

if __name__=="__main__":
    MainWindow()
    Gtk.main()