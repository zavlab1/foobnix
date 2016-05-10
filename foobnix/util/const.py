#-*- coding: utf-8 -*-
'''
Created on 30 авг. 2010

@author: ivan
'''
from foobnix.util.localization import foobnix_localization
import locale
from gi.repository import Gtk

foobnix_localization()

SITE_LOCALE = "en"
if locale.getdefaultlocale()[0] and ("ru" in locale.getdefaultlocale()[0]):
    SITE_LOCALE = "ru"

ORDER_LINEAR = "ORDER_LINEAR"
ORDER_SHUFFLE = "ORDER_SHUFFLE"
ORDER_RANDOM = "ORDER_RANDOM"

REPEAT_ALL = "REPEAT_ALL"
REPEAT_SINGLE = "REPEAT_SINGLE"
REPEAT_NO = "REPEAT_NO"


ON_CLOSE_CLOSE = "ON_CLOSE_CLOSE"
ON_CLOSE_HIDE = "ON_CLOSE_HIDE"
ON_CLOSE_MINIMIZE = "ON_CLOSE_MINIMIZE"

PLAYLIST_PLAIN = "PLAYLIST_PLAIN"
PLAYLIST_TREE = "PLAYLIST_TREE"

EQUALIZER_LABLES = ["PREAMP", "29", "59", "119", "237", "474", "1K", "2K", "4K", "8K", "15K"]


STATE_STOP = "STOP"
STATE_PLAY = "PLAY"
STATE_PAUSE = "PAUSE"

FTYPE_NOT_UPDATE_INFO_PANEL = "FTYPE_NOT_UPDATE_INFO_PANEL"

FTYPE_RADIO = "FTYPE_RADIO"

DOWNLOAD_STATUS_ALL = _("All")
DOWNLOAD_STATUS_ACTIVE = _("Active")
DOWNLOAD_STATUS_STOP = _("Stop")
DOWNLOAD_STATUS_DOWNLOADING = _("Downloading")
DOWNLOAD_STATUS_COMPLETED = _("Complete")
DOWNLOAD_STATUS_INACTIVE = _("Inactive")

DOWNLOAD_STATUS_LOCK = _("Lock")
DOWNLOAD_STATUS_ERROR = _("Error")

ICON_FOOBNIX = "images/hicolor/scalable/apps/foobnix.svg"

ICON_FOOBNIX_PLAY = "images/hicolor/scalable/actions/foobnix-play.svg"
ICON_FOOBNIX_PAUSE = "images/hicolor/scalable/actions/foobnix-pause.svg"
ICON_FOOBNIX_STOP = "images/hicolor/scalable/actions/foobnix-stop.svg"
ICON_FOOBNIX_RADIO = "images/hicolor/scalable/actions/foobnix-radio.svg"
ICON_BLANK_DISK = "images/foobnix-blank-disc.jpg"

ICON_FOOBNIX_PATH = "images/hicolor/scalable/apps/foobnix.svg"

ICON_FOOBNIX_PLAY_PATH = "images/hicolor/scalable/actions/foobnix-play.svg"
ICON_FOOBNIX_PAUSE_PATH = "images/hicolor/scalable/actions/foobnix-pause.svg"
ICON_FOOBNIX_STOP_PATH = "images/hicolor/scalable/actions/foobnix-stop.svg"
ICON_FOOBNIX_RADIO_PATH = "images/hicolor/scalable/actions/foobnix-radio.svg"
ICON_BLANK_DISK_PATH = "images/foobnix-blank-disc.jpg"

BEFORE = Gtk.TreeViewDropPosition.BEFORE
AFTER = Gtk.TreeViewDropPosition.AFTER
INTO_OR_BEFORE = Gtk.TreeViewDropPosition.INTO_OR_BEFORE
INTO_OR_AFTER = Gtk.TreeViewDropPosition.INTO_OR_AFTER