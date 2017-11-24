import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo ComboBox y ListStore")

        cajaV= Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)
        #añadimos una lista al modelo con la funcion append
        modelo=Gtk.ListStore(int,str)
        modelo.append([1, "Elemento 1"])
        modelo.append([2, "Elemento 2"])
        modelo.append([3, "Elemento 3"])
        modelo.append([4, "Elemento 4"])
        modelo.append([5, "Elemento 5"])
        modelo.append([6, "Elemento 6"])

        #añadimos el modelo al crear el ComboBox
        combo1= Gtk.ComboBox.new_with_model_and_entry(modelo)
        combo1.connect("changed",self.on_combo1_changed)
        #Este evento salta cuando pulsamo enter en el comboBox, si el cursor no esta dentro del entry
        combo1.connect("key_press_event",self.on_combo1_enter_key)
        #
        combo1.get_child().connect("activate", self.on_combo1_child_enter_key,combo1)
        #cuando iniciemos el formulario con set entry le decimos que se pondra en el primer elemento
        combo1.set_entry_text_column(1)
        cajaV.pack_start(combo1,False,False,0)

        self.add(cajaV)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()

    def on_combo1_changed(self,combo):
        puntero=combo.get_active_iter()
        modelo = combo.get_model()
        if puntero != None :
            #Esto [:2] es igual que hacer [0] y [1], pero en una sola linea
            id_fila, texto = modelo [puntero][:2]
            #los %s %d son elementos que indicamos tras el % que hay despues del string
            print ("selecionado: ID= %d, texto=%s" % (id_fila,texto))

    def on_combo1_enter_key(self,combo,key_pressed):
        if (key_pressed.keyval==65293):
            modelo=combo.get_model()
            nuevoTexto = combo.get_child()
            print("Insertado: %s" % nuevoTexto.get_text(),self)
            modelo.append([7, nuevoTexto.get_text()])

    def on_combo1_child_enter_key(self,entry,combo):
            modelo=combo.get_model()
            nuevoTexto = combo.get_child()
            print("Insertado: %s" % nuevoTexto.get_text())
            modelo.append([7, nuevoTexto.get_text()])

if __name__=="__main__":
    MainWindow()
    Gtk.main()

