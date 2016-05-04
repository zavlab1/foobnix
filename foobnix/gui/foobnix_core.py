#-*- coding: utf-8 -*-

import logging
import os
from gi.repository import Gtk

import sys

from foobnix.fc.fc import FC
from foobnix.gui.notetab import NoteTabControl
from foobnix.gui.base_layout import BaseFoobnixLayout
from foobnix.gui.base_controls import BaseFoobnixControls
from foobnix.gui.perspectives.fsperspective import FSPerspective
from foobnix.gui.perspectives.info import InfoPerspective
from foobnix.gui.perspectives.lastfm import LastFMPerspective
from foobnix.gui.perspectives.radio import RadioPerspective
from foobnix.gui.perspectives.storage import StoragePerspective
from foobnix.gui.perspectives.vk import VKPerspective
from foobnix.gui.window import MainWindow
from foobnix.gui.controls.playback import PlaybackControls, \
    OrderShuffleControls
from foobnix.gui.search import SearchControls
from foobnix.gui.controls.search_progress import SearchProgress
from foobnix.gui.engine.gstreamer import GStreamerEngine
from foobnix.gui.controls.seekbar import SeekProgressBarControls
from foobnix.gui.controls.volume import VolumeControls
from foobnix.gui.controls.status_bar import StatusbarControls
from foobnix.gui.controls.tray_icon import TrayIconControls
from foobnix.preferences.preferences_window import PreferencesWindow
from foobnix.gui.top import TopWidgets
from foobnix.eq.eq_controller import EqController
from foobnix.dm.dm import DM
from foobnix.util.single_thread import SingleThread
from foobnix.gui.perspectives.controller import Controller
from foobnix.util.localization import foobnix_localization
from foobnix.gui.service.lastfm_service import LastFmService
from foobnix.gui.controls.record import RadioRecord
from foobnix.gui.coverlyrics import CoverLyricsPanel
from foobnix.util.net_wrapper import NetWrapper


foobnix_localization()

class FoobnixCore(BaseFoobnixControls):
    def __init__(self, with_dbus=True):
        BaseFoobnixControls.__init__(self)
        self.layout = None

        self.init_icons()

        self.net_wrapper = NetWrapper(self, FC().net_ping)

        self.statusbar = StatusbarControls(self)

        self.lastfm_service = LastFmService(self)

        self.media_engine = GStreamerEngine(self)

        """elements"""

        self.volume = VolumeControls(self)

        self.record = RadioRecord(self)
        self.seek_bar_movie = SeekProgressBarControls(self)
        self.seek_bar = SeekProgressBarControls(self, self.seek_bar_movie)

        self.trayicon = TrayIconControls(self)
        self.main_window = MainWindow(self)

        self.notetabs = NoteTabControl(self)
        self.search_progress = SearchProgress(self)
        self.in_thread = SingleThread(self.search_progress)

        #self.movie_window = MovieDrawingArea(self)

        self.searchPanel = SearchControls(self)
        self.os = OrderShuffleControls(self)
        self.playback = PlaybackControls(self)

        self.perspectives = Controller(self)

        self.perspectives.attach_perspective(FSPerspective(self))
        self.perspectives.attach_perspective(VKPerspective(self))
        self.perspectives.attach_perspective(LastFMPerspective(self))
        self.perspectives.attach_perspective(RadioPerspective(self))
        self.perspectives.attach_perspective(StoragePerspective(self))
        self.perspectives.attach_perspective(InfoPerspective(self))

        self.coverlyrics = CoverLyricsPanel(self)

        """preferences"""
        self.preferences = PreferencesWindow(self)

        self.eq = EqController(self)
        self.dm = DM(self)

        """layout panels"""
        self.top_panel = TopWidgets(self)

        """layout"""
        self.layout = BaseFoobnixLayout(self)

        self.dbus = None
        if with_dbus:
            from foobnix.gui.controls.dbus_manager import DBusManager
            self.dbus = DBusManager(self)
        try:
            from foobnix.preferences.configs.hotkey_conf import load_foobnix_hotkeys
            load_foobnix_hotkeys()
        except:
            logging.warning("Can't to load keybinder library")

    def run(self):
        self.on_load()
        if FC().hide_on_start:
            self.main_window.hide()

    def init_icons(self):
        dir = os.path.join("foobnix", "share", "images")
        local_dir = os.path.join(sys.path[0], dir)
        if os.path.exists(local_dir):
            Gtk.IconTheme.get_default().append_search_path(local_dir)
        else:
            system_dir = os.path.abspath(os.path.join(os.sep, "usr", "share", "foobnix", "share", "images"))
            Gtk.IconTheme.get_default().append_search_path(system_dir)
