#-*- coding: utf-8 -*-
'''
Created on 3 окт. 2010

@author: ivan
'''

import logging
import os.path, sys


def get_foobnix_resourse_path_by_name(filename):
    if not filename:
        return None

    dir = os.path.join(sys.path[0], "share")
    prefix = sys.path[0] if os.path.exists(dir) else os.path.abspath(os.path.join(os.sep, "usr"))

    paths = [os.path.join(prefix, "share"),
             os.path.join(prefix, "share","foobnix"),
             "./",
             filename]

    for path in paths:
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            return full_path

    if filename.startswith("images"):
        return get_foobnix_resourse_path_by_name(filename.replace("images", "icons", 1))

    logging.error("File " + filename + " not found")
    raise TypeError("******* WARNING: File " + filename + " not found *******")
