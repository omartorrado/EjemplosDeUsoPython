import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Ejemplo de TreeView")
        self.set_default_size(400,300)
        self.set_border_width(20)

        columnas =["Nombre","Apellido","Telefono","Fijo"]

        agenda=[["Pepe","Perez","986666666",True],
                ["Ana","Alonso","123321123",False],
                ["Oscar","Rodriguez","746936759",False],
                ["Rosa","Lopez","986123321",True]]

        modelo = Gtk.ListStore(str,str,str,bool)

        for persona in agenda:
            #modelo.append(persona[0],persona[1],persona[2],persona[3])
            modelo.append(persona)

        vista=Gtk.TreeView(model=modelo)
        for i in range(len(columnas)):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
            vista.append_column(columna)

        cajaH= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaH.pack_start(vista,False,False,0)

        self.add(cajaH)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()