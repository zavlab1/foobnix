from foobnix.gui.controls.filter import FilterControl

__author__ = 'popsul'

from gi.repository import Gtk
from gi.repository import Gdk
from foobnix.util import analytics
from foobnix.gui.state import LoadSave, Quitable, Filterable
from foobnix.gui.perspectives import StackableWidget, BasePerspective, OneButtonToggled
from foobnix.helpers.my_widgets import PerspectiveButton


class Controller(Gtk.Box, LoadSave, Quitable, Filterable):

    def __init__(self, controls):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.add(self)
        self.scroll.set_border_width(0)
        viewport = self.scroll.get_child()
        viewport.set_shadow_type(Gtk.ShadowType.NONE)
        self.perspectives_container = StackableWidget()
        self.button_container = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
        self.button_controller = OneButtonToggled()
        self.perspectives = {}
        self.set_buttons_style()

        ## internal property
        self._perspectives = []

        self.filter = FilterControl(self)

        self.pack_start(self.perspectives_container, True, True, 0)
        self.pack_start(self.filter, False, False, 0)
        self.pack_start(self.button_container, False, False, 0)

        ## insert dummy page
        self.perspectives_container.add(Gtk.Label.new(""))
        self.show_all()

    def set_buttons_style(self):
        self.set_name("perspective")
        provider = Gtk.CssProvider.new()
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        provider.load_from_data("""
                                    #perspective .button {
                                        padding-left: 5;
                                        padding-right: 5;
                                    } """)

    def attach_perspective(self, perspective):
        assert isinstance(perspective, BasePerspective)
        perspective_id = perspective.get_id()
        self.perspectives[perspective_id] = perspective
        self._perspectives.append(perspective)
        widget = perspective.get_widget()
        perspective.widget_id = self.perspectives_container.add(widget)
        button = PerspectiveButton(perspective.get_name(), perspective.get_icon(), perspective.get_tooltip())

        def toggle_handler(btn, handler, *args):
            if btn.get_active():
                handler()
        button.connect("toggled", toggle_handler, lambda *a: self.activate_perspective(perspective_id))
        perspective.button = button
        self.button_container.pack_start(button, False, False, 0)
        self.button_controller.add_button(button)

    def activate_perspective(self, perspective_id):
        if self.is_activated(perspective_id):
            return
        perspective = self.get_perspective(perspective_id)
        assert perspective
        for _id in self.perspectives.keys():
            if self.is_activated(_id):
                self.get_perspective(_id).emit("deactivated")
        self.perspectives_container.set_active_by_index(perspective.widget_id)
        perspective.button.set_active(True)
        if isinstance(perspective, Filterable):
            self.filter.show()
        else:
            self.filter.hide()
        perspective.emit("activated")
        analytics.action("PERSPECTIVE_" + perspective.get_id())
        self.check_availability()

    def check_availability(self):
        for perspective in self._perspectives:
            if not perspective.is_available():
                perspective.button.set_sensitive(False)
                perspective.button.set_tooltip_text("Not available")
                if self.is_activated(perspective.get_id()):
                    self.activate_perspective(self._perspectives[0].get_id())
            else:
                perspective.button.set_sensitive(True)
                perspective.button.set_tooltip_text(perspective.get_tooltip())

    def is_activated(self, perspective_id):
        perspective = self.get_perspective(perspective_id)
        assert perspective
        return perspective.widget_id == self.perspectives_container.get_active_index()

    def get_perspective(self, perspective_id):
        if perspective_id in self.perspectives:
            return self.perspectives[perspective_id]
        return None

    def filter_by_file(self, value):
        for perspective in self._perspectives:
            if isinstance(perspective, Filterable):
                perspective.filter_by_file(value)

    def filter_by_folder(self, value):
        for perspective in self._perspectives:
            if isinstance(perspective, Filterable):
                perspective.filter_by_folder(value)

    def on_load(self):
        for perspective in self._perspectives:
            if isinstance(perspective, LoadSave):
                perspective.on_load()
        self.activate_perspective(self._perspectives[0].get_id())

    def on_save(self):
        for perspective in self._perspectives:
            if isinstance(perspective, LoadSave):
                perspective.on_save()

    def on_quit(self):
        for perspective in self._perspectives:
            if isinstance(perspective, Quitable):
                perspective.on_quit()
