#-*- coding: utf-8 -*-
'''
Created on 30 авг. 2010

@author: ivan
'''

import locale

from gi.repository import Gtk

from foobnix.util.localization import foobnix_localization

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

#---------------- icon names BEGIN ------------------

ICON_FOOBNIX_NAME = "foobnix"
ICON_FOOBNIX_SYMBOLIC_NAME = "foobnix-symbolic"

ICON_FOOBNIX_PLAY_NAME = "foobnix-play"
ICON_FOOBNIX_PAUSE_NAME = "foobnix-pause"
ICON_FOOBNIX_STOP_NAME = "foobnix-stop"
ICON_FOOBNIX_RADIO_NAME = "foobnix-radio"

ICON_FOOBNIX_PLAY_SYMBOLIC_NAME = "foobnix-play-symbolic"
ICON_FOOBNIX_PAUSE_SYMBOLIC_NAME = "foobnix-pause-symbolic"
ICON_FOOBNIX_STOP_SYMBOLIC_NAME = "foobnix-stop-symbolic"
ICON_FOOBNIX_RADIO_SYMBOLIC_NAME = "foobnix-radio-symbolic"

ICON_FOOBNIX_PLAY_ALT_NAME = "foobnix-play-alt-symbolic"
ICON_FOOBNIX_PAUSE_ALT_NAME = "foobnix-pause-alt-symbolic"
ICON_FOOBNIX_STOP_ALT_NAME = "foobnix-stop-alt-symbolic"

ICON_FOOBNIX_PLAY_ALT_SYMBOLIC_NAME = "foobnix-play-alt-symbolic"
ICON_FOOBNIX_PAUSE_ALT_SYMBOLIC_NAME = "foobnix-pause-alt-symbolic"
ICON_FOOBNIX_STOP_ALT_SYMBOLIC_NAME = "foobnix-stop-alt-symbolic"

ICON_BLANK_DISK_NAME = "foobnix-blank-disc"

#---------------- icon names END --------------------

#---------------- icon paths BEGIN ------------------

ICON_FOOBNIX = "icons/hicolor/scalable/apps/foobnix.svg"
ICON_FOOBNIX_SYMBOLIC = "icons/hicolor/scalable/apps/foobnix-symbolic.svg"
ICON_FOOBNIX_ALT = "images/foobnix-tux.gif"

ICON_FOOBNIX_PLAY  = "icons/hicolor/scalable/apps/foobnix.svg"
ICON_FOOBNIX_PAUSE = "icons/hicolor/scalable/actions/foobnix-pause.svg"
ICON_FOOBNIX_STOP  = "icons/hicolor/scalable/actions/foobnix-stop.svg"
ICON_FOOBNIX_RADIO = "icons/hicolor/scalable/actions/foobnix-radio.svg"

ICON_FOOBNIX_PLAY_SYMBOLIC  = "icons/hicolor/scalable/apps/foobnix-symbolic.svg"
ICON_FOOBNIX_PAUSE_SYMBOLIC = "icons/hicolor/scalable/actions/foobnix-pause-symbolic.svg"
ICON_FOOBNIX_STOP_SYMBOLIC  = "icons/hicolor/scalable/actions/foobnix-stop-symbolic.svg"
ICON_FOOBNIX_RADIO_SYMBOLIC = "icons/hicolor/scalable/actions/foobnix-radio-symbolic.svg"

ICON_FOOBNIX_PLAY_ALT  = "icons/hicolor/scalable/actions/foobnix-play-alternate.svg"
ICON_FOOBNIX_PAUSE_ALT = "icons/hicolor/scalable/actions/foobnix-pause-alternate.svg"
ICON_FOOBNIX_STOP_ALT  = "icons/hicolor/scalable/actions/foobnix-stop-alternate.svg"

ICON_FOOBNIX_PLAY_ALT_SYMBOLIC  = "icons/hicolor/scalable/actions/foobnix-play-alternate-symbolic.svg"
ICON_FOOBNIX_PAUSE_ALT_SYMBOLIC = "icons/hicolor/scalable/actions/foobnix-pause-alternate-symbolic.svg"
ICON_FOOBNIX_STOP_ALT_SYMBOLIC  = "icons/hicolor/scalable/actions/foobnix-stop-alternate-symbolic.svg"

ICON_BLANK_DISK_PATH = "images/foobnix-blank-disc.jpg"

#---------------- icon paths END --------------------

BEFORE = Gtk.TreeViewDropPosition.BEFORE
AFTER = Gtk.TreeViewDropPosition.AFTER
INTO_OR_BEFORE = Gtk.TreeViewDropPosition.INTO_OR_BEFORE
INTO_OR_AFTER = Gtk.TreeViewDropPosition.INTO_OR_AFTER