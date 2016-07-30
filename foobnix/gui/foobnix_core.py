#-*- coding: utf-8 -*-

import logging

from foobnix.dm.dm import DM
from foobnix.eq.eq_controller import EqController
from foobnix.fc.fc import FC
from foobnix.gui.base_controls import BaseFoobnixControls
from foobnix.gui.base_layout import BaseFoobnixLayout
from foobnix.gui.controls.playback import PlaybackControls, \
                                          OrderShuffleControls
from foobnix.gui.controls.record import RadioRecord
from foobnix.gui.controls.search_progress import SearchProgress
from foobnix.gui.controls.seekbar import SeekProgressBarControls
from foobnix.gui.controls.status_bar import StatusbarControls
from foobnix.gui.controls.tray_icon import TrayIconControls
from foobnix.gui.controls.volume import VolumeControls
from foobnix.gui.coverlyrics import CoverLyricsPanel
from foobnix.gui.engine.gstreamer import GStreamerEngine
from foobnix.gui.notetab import NoteTabControl
from foobnix.gui.perspectives.controller import Controller
from foobnix.gui.perspectives.fsperspective import FSPerspective
from foobnix.gui.perspectives.info import InfoPerspective
from foobnix.gui.perspectives.lastfm import LastFMPerspective
from foobnix.gui.perspectives.radio import RadioPerspective
from foobnix.gui.perspectives.storage import StoragePerspective
from foobnix.gui.perspectives.vk import VKPerspective
from foobnix.gui.search import SearchControls
from foobnix.gui.top import TopWidgets
from foobnix.gui.window import MainWindow
from foobnix.helpers.icons import init_icons
from foobnix.preferences.preferences_window import PreferencesWindow
from foobnix.service.lastfm_service import LastFmService
from foobnix.util.localization import foobnix_localization
from foobnix.util.net_wrapper import NetWrapper
from foobnix.util.single_thread import SingleThread

foobnix_localization()


class FoobnixCore(BaseFoobnixControls):
    def __init__(self, with_dbus=True):
        BaseFoobnixControls.__init__(self)
        self.layout = None

        init_icons()

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
