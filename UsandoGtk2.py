import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Titulo: Usando Gtk.Scale y Gtk.label")
        #spacing es la separacion entre controles de la caja
        self.caja=Gtk.Box(spacing = 6)
        #añadimos la caja a la ventana
        self.add(self.caja)
        #creamos una etiqueta y subrayamos de azul el texto
        self.etiqueta = Gtk.Label()
        self.etiqueta.set_markup("<span background='blue'>Etiqueta</span>")
        #añadimos la etiqueta a la caja
        self.caja.pack_start(self.etiqueta, True, True, 2)
        #Creamos un objeto escala, le asignamos un evento change-value y lo añadimos a la caja
        self.escala=Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 1,100,1)
        self.escala.connect("change-value",self.on_escala_change_value)
        self.caja.pack_start(self.escala, True, True, 2)
        #añadimos el evento de cerrar ventana
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()

    def on_escala_change_value(self,objeto,a,b):
        #print(objeto)
        #print(a)
        print(b)
if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()