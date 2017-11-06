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
        self.boton1=Gtk.Button(label="Resto")
        self.boton2 = Gtk.Button(label="Potencia")
        self.boton3 = Gtk.Button(label="Raiz")

        self.label1 = Gtk.Label("Resultado: \n 666")

        self.entry1= Gtk.Entry()
        self.entry2= Gtk.Entry()

        #Los añadimos al grid (widget, columna, fila, anchoEnColumnas, altoEnFilas)
        self.grid.attach(self.boton1,0,0,1,1)
        self.grid.attach(self.label1,0,1,1,2)
        self.grid.attach_next_to(self.entry1,self.boton1,Gtk.PositionType.RIGHT ,2,1)
        self.grid.attach(self.entry2,1,1,2,1)
        self.grid.attach(self.boton2,1,2,1,1)
        self.grid.attach_next_to(self.boton3,self.boton2,Gtk.PositionType.RIGHT,1,1)

        #Asignamos las acciones a cada widget
        self.boton1.connect("clicked",self.action_resto)
        self.boton2.connect("enter", self.action_potencia)
        #Para pasarle parametros a una funcion, se pondrian a continuacion del nombre de la funcion
        self.boton2.connect("leave",self.action_potencia_b,2,7,"Pasando parametros \n a la funcion que \n ejecuta EL BOTON")
        self.boton3.connect("pressed", self.action_raiz)

        #Mostramos todo_ el contenido de la ventana principal
        self.show_all()

    #Creamos las acciones de cada widget
    def action_resto(self,evento):
        primerNumero= float(self.entry1.get_text())
        segundoNumero = float(self.entry2.get_text())
        self.label1.set_text(str(primerNumero%segundoNumero))

    def action_potencia(self,evento):
        primerNumero = float(self.entry1.get_text())
        segundoNumero = float(self.entry2.get_text())
        self.label1.set_text(str(primerNumero ** segundoNumero))

    def action_potencia_b(self,evento,num,num2,texto):
        self.entry1.set_text(str(num))
        self.entry2.set_text(str(num2))
        self.label1.set_text(texto)

    def action_raiz(self,evento):
        primerNumero = float(self.entry1.get_text())
        segundoNumero = float(self.entry2.get_text())
        self.label1.set_text(str(primerNumero ** (1/segundoNumero)))

if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()
