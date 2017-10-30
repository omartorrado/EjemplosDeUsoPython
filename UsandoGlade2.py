import gi
import time

from gi.overrides import Gdk

gi.require_version("Gtk",'3.0')
from gi.repository import Gtk


class VentanaPrincipal:

    def __init__(self):
        ruta= "/home/local/DANIELCASTELAO/otorradomiguez/PycharmProjects/EjemplosDeUso/UsandoGlade2.glade"
        builder = Gtk.Builder()
        builder.add_from_file(ruta)
        self.ventana=builder.get_object("ventanaPrincipal")
        self.ventana.show_all()
        self.labelColor=builder.get_object("labelColor")
        eventos = {"mainWindow_Destroy": Gtk.main_quit,
                   "botonVerdeClicked": self.botonClicked,
                   "botonAzulClicked": self.botonClicked,
                   "botonAmarilloClicked": self.botonClicked,
                   "botonRojoClicked": self.botonClicked}
        builder.connect_signals(eventos)

    def botonClicked(self,evento):
        if evento.get_label()=="verde":
            #Cambiamos el color de fondo
            self.labelColor.modify_bg(Gtk.StateType.NORMAL,Gdk.color_parse("green"))
            print("verde")
        elif evento.get_label()=="azul":
            #Subrayamos el texto con un color
            self.labelColor.set_markup("<span background='blue'>"+self.labelColor.get_text()+"</span>")
            print("azul")
        elif evento.get_label()=="amarillo":
            self.labelColor.set_markup("<span background='yellow'>"+self.labelColor.get_text()+"</span>")
            print("amarillo")
        elif evento.get_label()=="rojo":
            self.labelColor.set_markup("<span background='red'>"+self.labelColor.get_text()+"</span>")
            print("rojo")


if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()