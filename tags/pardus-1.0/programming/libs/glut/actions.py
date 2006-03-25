#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.cd("src/glut/glx")
    autotools.make()

def install():
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")

    shelltools.copy("include/GL","%s/usr/include/GL" % get.installDIR())
    shelltools.copy("lib/*","%s/usr/lib/" % get.installDIR())

    pisitools.remove("/usr/lib/libglut.so.3")
    pisitools.dosym("/usr/lib/libglut.so.3.7.1","/usr/lib/libglut.so.3")
