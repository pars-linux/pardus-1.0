#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "jpeg-mmx"

def setup():
    autotools.configure("--enable-shared")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/include/jpeg-mmx")
    pisitools.dodir("/usr/lib")
    autotools.rawInstall("includedir=%s/usr/include/jpeg-mmx prefix=%s/usr" % (get.installDIR(), get.installDIR()))
    pisitools.dodoc("README", "change.log", "structure.doc", "libjpeg.doc")

    pisitools.domove("/usr/lib/libjpeg.la", "/usr/lib", "libjpeg-mmx.la")
    pisitools.domove("/usr/lib/libjpeg.so.62.0.0", "/usr/lib", "libjpeg-mmx.so.62.0.0")
    
    pisitools.remove("/usr/lib/libjpeg.so")
    pisitools.remove("/usr/lib/libjpeg.so.62")
    
    pisitools.dosym("/usr/lib/libjpeg-mmx.so.62.0.0", "/usr/lib/libjpeg-mmx.so")
    pisitools.dosym("/usr/lib/libjpeg-mmx.so.62.0.0", "/usr/lib/libjpeg-mmx.so.62")
