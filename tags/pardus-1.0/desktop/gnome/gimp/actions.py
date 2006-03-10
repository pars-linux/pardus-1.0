#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gürer Özen <gurer@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# FIXME: following flags should be activated when needed packages
# become available
# with-python, needs pygtk
# enable-print, needs libgimpprint

def setup():
    autotools.configure("--with-x \
                        --disable-gtk-doc \
                        --disable-default-binary \
                        --disable-print \
                        --disable-python \
                        --with-libjpeg \
                        --with-libexif \
                        --with-png \
                        --with-librsvg \
                        --with-lcms \
                        --with-tiff \
                        --with-aa")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/applications")
    pisitools.dodir("/usr/share/application-registry")
    pisitools.dodir("/usr/share/mime-info")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dosym("gimp-remote-2.3", "/usr/bin/gimp-remote")
    pisitools.dosym("gimp-2.3", "/usr/bin/gimp")
    
    pisitools.dodoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README*")
