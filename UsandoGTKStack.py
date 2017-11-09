import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Ejemplo de Gtk.Stack y Gtk.StackSwitcher")

        cajaV=Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing= 6)
        self.add(cajaV)

        stack=Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        chkButton=Gtk.CheckButton("Púlsame")
        stack.add_titled(chkButton, "Púlsame","Boton Púlsame")

        label1=Gtk.Label()
        label1.set_markup("<big> A nosa etiqueta</big>")
        stack.add_titled(label1,"Etiqueta","Etiqueta para mostrar")

#El stack es donde estan las cosas, y el switcher las pestañas para cambiar entre ellos, funcionan en conjunto
        stackSelector=Gtk.StackSwitcher()
        stackSelector.set_stack(stack)

        cajaV.pack_start(stackSelector, True, True, 0)
        cajaV.pack_start(stack,True,True,0)

        self.connect("destroy",Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    ventana=VentanaPrincipal()
    Gtk.main()