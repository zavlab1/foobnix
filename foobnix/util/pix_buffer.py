'''
Created on Nov 4, 2010

@author: ivan
'''
import os
import urllib
from foobnix.gui.service.path_service import get_foobnix_resourse_path_by_name
from gi.repository import Gtk
from gi.repository import GdkPixbuf
import logging

def create_pixbuf_from_url(url, size):
    pixbuf = create_origin_pixbuf_from_url(url)
    if size:
        return resize_pixbuf(pixbuf, size)
    else:
        return pixbuf

def resize_pixbuf(pixbuf, size):
    if not pixbuf:
        return None
    if size:
        return pixbuf.scale_simple(size, size, GdkPixbuf.InterpType.BILINEAR) #@UndefinedVariable
    else:
        return pixbuf

def create_pixbuf_from_path(path, size=None):
    if not path:
        return None
    if not os.path.isfile(path):
        path = get_foobnix_resourse_path_by_name(path)
    if size:
        return GdkPixbuf.Pixbuf.new_from_file_at_size(path, size, size)
    else:
        return GdkPixbuf.Pixbuf.new_from_file(path) #@UndefinedVariable



def create_origin_pixbuf_from_url(url):
    f = urllib.urlopen(url)
    data = f.read()
    pbl = GdkPixbuf.PixbufLoader() #@UndefinedVariable
    pbl.write(data)
    pbuf = pbl.get_pixbuf()
    pbl.close()
    return pbuf
