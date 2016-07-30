#-*- coding: utf-8 -*-
'''
Created on 30 july 2016

@author: zavlab1
'''

import logging
import os
import sys

from gi.repository import Gtk


def init_icons():

    def add_to_theme(path):
        Gtk.IconTheme.get_default().append_search_path(path)
        logging.info("Directory " + path + " added to GtkIconTheme search paths")

    share_dir = os.path.join(sys.path[0], "share")

    if os.path.exists(share_dir):
        logging.info("Application run from source")

        app_icon_dir = os.path.join(share_dir, "foobnix", "images")
        sys_icon_dir = os.path.join(share_dir, "icons")
        add_to_theme(app_icon_dir)
        add_to_theme(sys_icon_dir)
    else:
        logging.info("Installed application is run")

        app_dir = os.path.abspath(os.path.join(os.sep, "usr", "share", "foobnix", "images"))
        add_to_theme(app_dir)


def icon_exists(icon_name):
    theme = Gtk.IconTheme.get_default()
    return theme.has_icon(icon_name)
