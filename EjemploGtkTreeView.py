import gi
gi.require_version("GdkPixbuf","2.0")
from gi.repository.GdkPixbuf import Pixbuf
gi.require_version("Gtk","3.0")
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Ejemplo de TreeView")
        self.set_default_size(400,300)
        self.set_border_width(20)

        columnas =["Nombre","Apellido","Telefono","Fijo","Icono"]

        agenda=[["Pepe","Perez","986666666",True,"gtk-add"],
                ["Ana","Alonso","123321123",False,"gtk-cdrom"],
                ["Oscar","Rodriguez","746936759",False,"gtk-cut"],
                ["Rosa","Lopez","986123321",True,"gtk-paste"]]

        modelo = Gtk.ListStore(str,str,str,bool,str)

        for persona in agenda:
            modelo.append(persona)

        vista=Gtk.TreeView(model=modelo)
        for i in range(len(columnas)-1):
            if(i==4):
                celda=Gtk.CellRendererPixbuf()
                columna= Gtk.TreeViewColumn(columnas[i],celda, pixbuf=i)
            elif(i==3):
                celda = Gtk.CellRendererToggle()
                columna = Gtk.TreeViewColumn(columnas[i], celda, active=i)
            else:
                celda = Gtk.CellRendererText()
                columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
            vista.append_column(columna)

        vista.get_selection().connect("changed",self.on_vista_changed)

        cajaH= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaH.pack_start(vista,False,False,0)

        self.add(cajaH)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()

    def on_vista_changed(self,seleccion):
        (modelo,puntero) = seleccion.get_selected()
        print("%s %s %s %s\n" %(modelo [puntero][0],modelo [puntero][1],modelo [puntero][2],modelo [puntero][3]))

if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()