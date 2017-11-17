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

        elementos =['Esta ','é','unha ','lista',"Fail",'con','ordenación','incluida ']
        elementosB = [1,2,3,4,9,10,11,12,13,14,15,16,17,18,5,6,7,8]

        for i in elementosB:
            listBox2.add(listBoxConDatos(i))

        #Esto ordenaria "alfabeticamente" (aunque si hay acentos los pone al final)
        def funcion_ordenacion(fila1,fila2, dato, notify_destroy):
            return fila1.dato.lower() < fila2.dato.lower()
        #Esta funcion ordena los numeros de menor a mayor
        def funcion_ordenacionB(fila1,fila2):
            return fila1.dato > fila2.dato
        #esto filtra, si el dato es "Fail" lo quita de la lista
        def funcion_filtro(fila,dato,notify_destroy):
            return False if fila.dato == "Fail" else True
        #Esta funcion filtra para que solo salgan los numeros pares
        def funcion_filtroB(fila):
            return False if fila.dato%2 !=0 else True

        #los metodos anteriores se los asignamos a la listBox como sigue con el set_sort_func y set_filter_func
        #listBox2.set_sort_func(funcion_ordenacion,None,False)
        #listBox2.set_filter_func(funcion_filtro,None,False)

        listBox2.set_sort_func(funcion_ordenacionB)
        listBox2.set_filter_func(funcion_filtroB)

        #row-activated es el evento de seleccionar una fila de la listBox
        listBox2.connect("row-activated", lambda control,fila : print(fila.dato))

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