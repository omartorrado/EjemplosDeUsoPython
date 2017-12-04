import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo de TreeView en arbol")
        self.set_default_size(800,600)
        self.set_border_width(10)

        modelo = Gtk.TreeStore(str,int)
        for abuelo in range(5):
            punteroAbuelo= modelo.append(None,["Abuelo",abuelo])
            for padre in range(3):
                punteroPadre= modelo.append(punteroAbuelo,["Padre %i del abuelo %i" % (padre,abuelo),padre])
                for hijo in range(4):
                    punteroHijo=modelo.append(punteroPadre,["Hijo %i del padre %i del abuelo %i" % (hijo,padre,abuelo),hijo])

        vista=Gtk.TreeView(model=modelo)
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Parentesco")
        vista.append_column(columna)
        columna.pack_start(celda,True)
        columna.add_attribute(celda,"text",0)

        columna2 = Gtk.TreeViewColumn("Orden",celda,text=1)
        vista.append_column(columna2)

#con el reorderable nos permite modificar la vista durante la ejecucion, pero sin guardarla para futuras ejecuciones
        vista.set_search_column(0)
        columna.set_sort_column_id(0)
        vista.set_reorderable(True)

        self.add(vista)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()
