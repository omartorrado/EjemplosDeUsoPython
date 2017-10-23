import gi
gi.require_version("Gtk",'3.0')
from gi.repository import Gtk


class MainWindow:

    def __init__(self):
        ruta= "/home/local/DANIELCASTELAO/otorradomiguez/PycharmProjects/EjemplosDeUso/GTKGUI.xml"
        builder = Gtk.Builder()
        builder.add_from_file(ruta)
        self.ventana=builder.get_object("window1")
        self.ventana.show_all()

if __name__=="__main__":
    MainWindow()
    Gtk.main()