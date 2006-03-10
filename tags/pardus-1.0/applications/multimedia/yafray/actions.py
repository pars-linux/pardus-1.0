#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.7")
    pisitools.dosed("*-settings.py", "-03", "%s -fsigned-char" % get.CXXFLAGS())

def build():
    scons.make("prefix='/usr'")

def install():
    insparam = 'prefix="/usr" destdir="%s" libdir="/lib" install' % get.installDIR()
    scons.install(insparam)

    #wtf?
    pisitools.removeDir("/usr/etc")
    pisitools.dodir("/etc")
    pisitools.insinto("/etc", "src/gram.yafray")

    pisitools.dodoc("AUTHORS")
    pisitools.dohtml("doc/doc.html")
