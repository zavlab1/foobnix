#-*- coding: utf-8 -*-
'''
Created on 24 авг. 2010

@author: ivan
'''

from gi.repository import Gtk

from foobnix.fc.fc import FC
from foobnix.util import const
from foobnix.preferences.config_plugin import ConfigPlugin
from foobnix.helpers.image import ImageBase
from foobnix.util.const import ICON_BLANK_DISK
from foobnix.gui.service.path_service import get_foobnix_resourse_path_by_name
from foobnix.helpers.pref_widgets import FrameDecorator, VBoxDecorator, ChooseDecorator, \
    IconBlock


class TrayIconConfig(ConfigPlugin):

    name = _("Tray Icon")

    def __init__(self, controls):
        self.controls = controls
        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.hide()

        '''static_icon'''
        self.static_icon = IconBlock(_("Icon"), controls, FC().static_icon_entry)

        """dynamic icons"""
        self.play_icon = IconBlock(_("Play"), controls, FC().play_icon_entry)
        self.pause_icon = IconBlock(_("Pause"), controls, FC().pause_icon_entry)
        self.stop_icon = IconBlock(_("Stop"), controls, FC().stop_icon_entry)
        self.radio_icon = IconBlock(_("Radio"), controls, FC().radio_icon_entry)

        self.hide_in_tray_on_start = Gtk.CheckButton.new_with_label(_("Hide player in tray on start"))
        self.tray_icon_button = Gtk.CheckButton.new_with_label(_("Show tray icon"))
        #self.tray_icon_button.connect("clicked", self.on_show_tray_icon)

        self.close_button = Gtk.RadioButton.new_with_label(None, _("On close window - close player"))

        self.hide_button = Gtk.RadioButton.new_with_label_from_widget(self.close_button, _("On close window - hide player"))
        self.hide_button.connect("toggled", self.on_show_tray_icon)

        self.minimize_button = Gtk.RadioButton.new_with_label_from_widget(self.close_button,_("On close window - minimize player"))

        """system icon"""
        self.static_tray_icon = ChooseDecorator(None, FrameDecorator(_("System Icon Static"), self.static_icon, 0.5, 0.5))

        """dynamic icons"""
        line = VBoxDecorator(self.play_icon,
                             self.pause_icon,
                             self.stop_icon,
                             self.radio_icon)

        self.icon_controls = ChooseDecorator(self.static_tray_icon.get_radio_button(), FrameDecorator(_("System Icons Dynamic"), line, 0.5, 0.5))

        """disc image icon"""
        image = ImageBase(ICON_BLANK_DISK, 30)
        self.change_tray_icon = ChooseDecorator(self.static_tray_icon.get_radio_button(), FrameDecorator(_("Disc cover image"), image, 0.5, 0.5))

        self.notifier = Gtk.CheckButton.new_with_label(_("Notification pop-up"))
        self.notifier.connect("toggled", self.on_toggle)

        self.n_time = self.notify_time()

        box.pack_start(self.hide_in_tray_on_start, False, True, 0)
        box.pack_start(self.tray_icon_button, False, True, 0)
        box.pack_start(self.close_button, False, True, 0)
        box.pack_start(self.hide_button, False, True, 0)
        box.pack_start(self.minimize_button, False, True, 0)

        box.pack_start(self.static_tray_icon, True, True, 0)
        box.pack_start(self.icon_controls, True, True, 0)
        box.pack_start(self.change_tray_icon, False, False, 0)

        notifier_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        notifier_box.pack_start(self.notifier, False, False, 0)
        notifier_box.pack_start(self.n_time, False, False, 0)
        box.pack_start(FrameDecorator(_("Notification"), notifier_box, 0.5, 0.5), False, False, 0)
        self.widget = box

    def on_show_tray_icon(self, *args):
        if not self.tray_icon_button.get_active():
            self.hide_button.set_sensitive(False)
            if self.hide_button.get_active():
                self.minimize_button.set_active(True)
            self.controls.trayicon.hide()
        else:
            self.controls.trayicon.show()
            self.hide_button.set_sensitive(True)

    def on_static_icon(self):
        if FC().static_tray_icon:
            FC().static_icon_entry = self.static_icon.get_active_path()
            self.controls.trayicon.set_from_file(FC().static_icon_entry)

    def check_active_dynamic_icon(self, icon_object):
        icon_name = icon_object.entry.get_text()
        try:
            path = get_foobnix_resourse_path_by_name(icon_name)
            self.controls.trayicon.set_from_file(path)
        except TypeError:
            pass

    def notify_time(self):
        label = Gtk.Label.new(_("Time Notification (sec): "))

        self.adjustment = Gtk.Adjustment(value=0, lower=1, upper=10, step_incr=0.5)

        not_len = Gtk.SpinButton.new(self.adjustment, 0.0, 0)
        not_len.show()

        hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        hbox.pack_start(label, False, False, 0)
        hbox.pack_start(not_len, False, False, 0)
        hbox.show_all()
        hbox.set_sensitive(False)

        return hbox

    def on_toggle(self, *a):
            if self.notifier.get_active():
                self.n_time.set_sensitive(True)
            else:
                self.n_time.set_sensitive(False)

    def on_load(self):
        self.tray_icon_button.set_active(FC().show_tray_icon)
        self.static_tray_icon.button.set_active(FC().static_tray_icon)
        self.icon_controls.button.set_active(FC().system_icons_dinamic)
        self.change_tray_icon.button.set_active(FC().change_tray_icon)
        self.hide_in_tray_on_start.set_active(FC().hide_on_start)

        if FC().on_close_window == const.ON_CLOSE_CLOSE:
            self.close_button.set_active(True)

        elif FC().on_close_window == const.ON_CLOSE_HIDE:
            self.hide_button.set_active(True)

        elif FC().on_close_window == const.ON_CLOSE_MINIMIZE:
            self.minimize_button.set_active(True)

        if FC().notifier:
            self.notifier.set_active(True)
            self.n_time.set_sensitive(True)
        self.adjustment.set_value(FC().notify_time / 1000)

        self.static_icon.entry.set_text(FC().static_icon_entry)
        self.play_icon.entry.set_text(FC().play_icon_entry)
        self.pause_icon.entry.set_text(FC().pause_icon_entry)
        self.stop_icon.entry.set_text(FC().stop_icon_entry)
        self.radio_icon.entry.set_text(FC().radio_icon_entry)

    def on_save(self):
        FC().show_tray_icon = self.tray_icon_button.get_active()
        FC().hide_on_start =  self.hide_in_tray_on_start.get_active()
        FC().static_tray_icon = self.static_tray_icon.button.get_active()

        if FC().static_tray_icon:
            self.on_static_icon()

        if FC().system_icons_dinamic:
            FC().play_icon_entry = self.play_icon.get_active_path()
            FC().pause_icon_entry = self.pause_icon.get_active_path()
            FC().stop_icon_entry = self.stop_icon.get_active_path()
            FC().radio_icon_entry = self.radio_icon.get_active_path()

        FC().system_icons_dinamic = self.icon_controls.button.get_active()

        FC().change_tray_icon = self.change_tray_icon.button.get_active()

        if  self.close_button.get_active():
            FC().on_close_window = const.ON_CLOSE_CLOSE

        elif self.hide_button.get_active():
            FC().on_close_window = const.ON_CLOSE_HIDE

        elif self.minimize_button.get_active():
            FC().on_close_window = const.ON_CLOSE_MINIMIZE

        if self.notifier.get_active():
            FC().notifier = True
        else:
            FC().notifier = False

        FC().static_icon_entry = self.static_icon.entry.get_text()
        FC().play_icon_entry = self.play_icon.entry.get_text()
        FC().pause_icon_entry = self.pause_icon.entry.get_text()
        FC().stop_icon_entry = self.stop_icon.entry.get_text()
        FC().radio_icon_entry = self.radio_icon.entry.get_text()
        FC().notify_time = int(self.adjustment.get_value() * 1000)

        if IconBlock.temp_list != FC().all_icons:
            FC().all_icons = IconBlock.temp_list

        self.on_show_tray_icon()