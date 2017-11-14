import gi
from moduloGrid import GridModificado
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio

class ventanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.Flowbox")

        self.set_default_size(500,350)
        self.set_border_width(5)

        cabeceira = Gtk.HeaderBar(title="Exemplo FlowBox")
        cabeceira.set_subtitle("Exemplo de headerBar")
        cabeceira.props.show_close_button = True


        btnBoton = Gtk.Button()
        icono = Gio.ThemedIcon(name ="mail-send-receive-symbolic")
        imaxe = Gtk.Image.new_from_gicon(icono,Gtk.IconSize.BUTTON)
        btnBoton.add(imaxe)
        cabeceira.pack_end(btnBoton)
        caixa = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(caixa.get_style_context(),"linked")
        btnFrechaI = Gtk.Button()
        btnFrechaI.add(Gtk.Arrow(Gtk.ArrowType.LEFT,Gtk.ShadowType.NONE))
        caixa.add(btnFrechaI)
        btnFrechaD = Gtk.Button()
        btnFrechaD.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        caixa.add(btnFrechaD)
        cabeceira.pack_start(caixa)
        #Configuración do FlowBox
        flowBox = Gtk.FlowBox()
        flowBox.set_valign(Gtk.Align.START)
        flowBox.set_max_children_per_line(30)
        flowBox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.crea_flowbox(flowBox)
        scroll = Gtk.ScrolledWindow()
        #Valores de set_policy(valor horizontal,valor vertical)
        scroll.set_policy(Gtk.PolicyType.NEVER,Gtk.PolicyType.AUTOMATIC)
        #metemos el flowbox al scrollbar
        scroll.add(flowBox)
        #y el scroll bar a la window
        self.add(scroll)
        self.set_titlebar(cabeceira)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()

    def crea_flowbox(self,flowbox):
        for i in range (20):
            flowbox.add(GridModificado())




if __name__ == "__main__":
    ventanaPrincipal()
    Gtk.main()