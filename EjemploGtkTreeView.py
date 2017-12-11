import gi
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
        for i in range(len(columnas)):
            if(i==4):
                celda=Gtk.CellRendererPixbuf()
                columna= Gtk.TreeViewColumn(columnas[i],celda, icon_name=i)
            elif(i==3):
                celda = Gtk.CellRendererToggle()
                celda.connect("toggled",self.on_celda_toggled, modelo)
                columna = Gtk.TreeViewColumn(columnas[i], celda, active=i)
            elif(i==2):
                celda = Gtk.CellRendererText(editable=True)
                columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
                celda.connect("edited",self.on_celda_edited,modelo)
            else:
                celda = Gtk.CellRendererText()
                columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)
            vista.append_column(columna)


        vista.get_selection().connect("changed",self.on_vista_changed)

        #En estas dos lineas definimos si va a ordenar en orden ascendente o descendente y la funcion que usa para ello
        modelo.set_sort_column_id(1,Gtk.SortType.ASCENDING)
        modelo.set_sort_func(1,self.compara_apellido,None)


        cajaH= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaH.pack_start(vista,False,False,0)

        self.add(cajaH)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()

    def on_vista_changed(self,seleccion):
        (modelo,puntero) = seleccion.get_selected()
        print("%s %s %s %s\n" %(modelo [puntero][0],modelo [puntero][1],modelo [puntero][2],modelo [puntero][3]))

    def on_celda_toggled(self,celda,puntero,modelo):
        modelo[puntero][3]=not modelo[puntero][3]

    def on_celda_edited(self,celda,posicion,texto,modelo):
        modelo[posicion][2]= texto

    def compara_apellido(self,modelo,fila1,fila2,datos):
        columna_ordenar=modelo.get_sort_column_id()
        valor1=modelo.get_value(fila1,columna_ordenar[0])
        valor2=modelo.get_value(fila2,columna_ordenar[0])
        #Asi ordenaria de alfabeticamente de forma inversa, cambiando los return o las condiciones cambiariamos como
        #ordena, por ejemplo si devolvemos -1,0,1 (en lugar de 1,0,-1 como ahora) ordenaria alfabeticamente
        #Esto tambien se ve influido por el orden ascendente o descendente que le hayamos indicado al sort_column_id
        if valor1<valor2:
            return 1
        elif valor1==valor2:
            return 0
        else:
            return -1

if __name__=="__main__":
    VentanaPrincipal()
    Gtk.main()