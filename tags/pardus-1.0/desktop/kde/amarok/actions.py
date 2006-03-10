#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@uludag.org.tr>

from pisi.actionsapi import kde

def setup():
    # amarok does not respect kde coding standards, and makes a lot of
    # assuptions regarding its installation directory. For this reason,
    # it must be installed in the KDE install directory.
    kde.configure("--with-arts \
                   --with-xine \
                   --with-gstreamer \
                   --with-opengl \
                   --with-libvisual \
                   --disable-debug")

def build():
    kde.make()

def install():
    kde.install()
