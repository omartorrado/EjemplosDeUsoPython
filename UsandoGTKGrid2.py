import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Usando Grid Layout")
        self.connect("delete-event",Gtk.main_quit)
        self.set_default_size(800,600)

        #Creamos el Grid Layout y lo añadimos a la ventana
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.grid.set_column_homogeneous = True
        self.grid.set_row_homogeneous = True

        #Creamos los widgets del interfaz
        self.boton2 = Gtk.Button(label="Aceptar")
        self.boton3 = Gtk.Button(label="Cancelar")

        self.label1 = Gtk.Label("Nombre: ")
        self.label2 = Gtk.Label("Contraseña: ")

        self.entry1= Gtk.Entry()
        self.entry2= Gtk.Entry()

        self.entry2.set_visibility(False)
        #Los añadimos al grid (widget, columna, fila, anchoEnColumnas, altoEnFilas)
        self.grid.attach(self.label1,0,0,1,1)
        self.grid.attach(self.label2,0,1,1,1)
        self.grid.attach_next_to(self.entry1,self.label1,Gtk.PositionType.RIGHT ,2,1)
        self.grid.attach(self.entry2,1,1,2,1)
        self.grid.attach(self.boton2,1,2,1,1)
        self.grid.attach_next_to(self.boton3,self.boton2,Gtk.PositionType.RIGHT,1,1)

        #Asignamos las acciones a cada widget


        #Mostramos todo_ el contenido de la ventana principal
        self.show_all()

    #Creamos las acciones de cada widget


if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()
