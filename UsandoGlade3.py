import gi
gi.require_version("Gtk",'3.0')
from gi.repository import Gtk


class VentanaPrincipal:

    def __init__(self):
        ruta= "/home/local/DANIELCASTELAO/otorradomiguez/PycharmProjects/EjemplosDeUso/UsandoGlade3.glade"
        builder = Gtk.Builder()
        builder.add_from_file(ruta)
        self.ventana=builder.get_object("ventanaPrincipal")
        self.ventana.show_all()
        eventos = {"Destroy": Gtk.main_quit,"valueChange":}
        builder.connect_signals(eventos)
        self.slider = builder.get_object("scale1")

    def valueChange(self):
        print("Terminar ejercicio")

if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()