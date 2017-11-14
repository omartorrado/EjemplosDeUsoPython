import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title ='Exemplo ListBox')
        self.set_border_width(5)


        caixaExterior =Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 4)
        self.add(caixaExterior)

        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        caixaExterior.pack_start(listBox,True,True,0)


        fila = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing =40)
        fila.add(caixaH)
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaH.pack_start(caixaV,True,True,0)

        etiqueta1 = Gtk.Label("Data e hora automática ",xalign =0)
        etiqueta2 = Gtk.Label("Require acceso  a interrede ", xalign=0)
        caixaV.pack_start(etiqueta1,True,True,0)
        caixaV.pack_start(etiqueta2,True,True,0)

        selector = Gtk.Switch()
        selector.props.valign = Gtk.Align.CENTER
        caixaH.pack_start(selector,False,True,0)
        listBox.add(fila)
        fila = Gtk.ListBoxRow()
        caixaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 50)
        self.connect("delete-event",Gtk.main_quit)
        fila.add(caixaH)
        etiqueta = Gtk.Label("Formato de data ",xalign=0)
        combo = Gtk.ComboBoxText()
        combo.insert(0,"0","24 -horas ")
        combo.insert(1,"1","AM/PM")
        caixaH.pack_start(etiqueta,True,True,0)
        caixaH.pack_start(combo,False, True, 0)
        listBox.add(fila)
        listBox2 = Gtk.ListBox()

        elementos =['Esta ','é','unha ','lista','con','ordenación','incluida ']

        for i in elementos:
            listBox2.add(listBoxConDatos(i))
        caixaExterior.pack_start(listBox2,True,True,0)
          #Funcións por definir
        self.show_all()
class listBoxConDatos(Gtk.ListBoxRow):

    def __init__(self,dato):

        super(Gtk.ListBoxRow,self).__init__()
        self.add(Gtk.Label(dato))
        self.dato = dato




if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()