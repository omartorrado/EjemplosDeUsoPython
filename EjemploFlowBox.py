import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gio

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Ejemplo de FlowBox y HeaderBar")

        self.set_default_size(600,400)
        self.set_border_width(100)

        cabecera=Gtk.HeaderBar(title="Titulo", subtitle="Subtitulo", show_close_button=True)

        boton1=Gtk.Button()
        icono=Gio.ThemedIcon(name="mail-send-receive-symbolic")
        imagen= Gtk.Image.new_from_gicon(icono, Gtk.IconSize.BUTTON)
        boton1.add(imagen)

        cabecera.pack_end(boton1)

        self.set_titlebar(cabecera)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    ventana=VentanaPrincipal()
    Gtk.main()

