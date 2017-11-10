import gi
import moduloGrid
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo de Gtk.Notebook")

        notebook=Gtk.Notebook()
        self.add(notebook)

        pagina1= Gtk.Box()
        pagina1.set_border_width(10)
        pagina1.add(Gtk.Label("Primera pagina"))
        #tenemos que hacer la pagina visible si queremos que se inicie en ella
        #si ninguna es visible se iniciará en la primera, pero si hay alguna visible inicia en la
        #primera que encuentra visible
        pagina1.set_visible(True)
        notebook.append_page(pagina1, Gtk.Label("Titulo de la pagina"))

        pagina2=Gtk.Box()
        pagina2.set_border_width(10)
        pagina2.add(Gtk.Label("Pagina con imagen y titulo"))
        #Podemos usar tanto el set_visible como el show_all para mostrarla
        pagina2.show_all()
        notebook.append_page(pagina2,Gtk.Image.new_from_icon_name("help-about",Gtk.IconSize.MENU))

        pagina3=moduloGrid.GridModificado()
        notebook.append_page(pagina3,Gtk.Label("Titulo pagina 3"))
    #La clase notebook no cambia a una pagina(al widget que la conforma) si esta no es visible
        notebook.set_current_page(1)

        self.connect("delete-event",Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    ventana=VentanaPrincipal()
    Gtk.main()