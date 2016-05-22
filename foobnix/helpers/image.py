'''
Created on Sep 28, 2010

@author: ivan
'''

import logging
import os
from gi.repository import Gtk

from foobnix.service.path_service import get_foobnix_resourse_path_by_name
from foobnix.util import idle_task
from foobnix.util.const import ICON_FOOBNIX
from foobnix.util.pix_buffer import create_pixbuf_from_url, create_pixbuf_from_path


class ImageBase(Gtk.Image):
    def __init__(self, resource, size=None):
        Gtk.Image.__init__(self)
        self._resource = resource
        self._size = size
        self._pixbuf = None
        self.set_image(resource, size)

    def set_no_image(self):
        self.set_image(ICON_FOOBNIX)

    @idle_task
    def _set_from_pixbuf(self):
        super(ImageBase, self).set_from_pixbuf(self._pixbuf)

    def _set_image_from_url(self, url, size):
        self._pixbuf = create_pixbuf_from_url(url, size)
        self._resource = url

    def _set_image_from_path(self, path, size):
        if not os.path.isfile(path):
            path = get_foobnix_resourse_path_by_name(path)

        self._pixbuf = create_pixbuf_from_path(path, size)

        logging.debug("Change icon path %s" % path)
        self._resource = path

    def set_image(self, image, size=None):
        if not size:
            size = self._size
        try:
            if image.startswith("http://"):
                self._set_image_from_url(image, size)
            else:
                self._set_image_from_path(image, size)
        except Exception as e:
            logging.error("Can't set image. " + str(e))
            return
        self._size = size
        self._set_from_pixbuf()

    def get_pixbuf(self):
        return self._pixbuf

    def get_size(self):
        return self._size

    def get_resource(self):
        return self._resource

    def set_size(self, size):
        self.set_image(self._resource, size)

    def set_resource(self, resource):
        self.set_image(resource)

    def update_image_from(self, bean):
        if not bean or not bean.image:
            self.set_no_image()
        else:
            self.set_image(bean.image)
