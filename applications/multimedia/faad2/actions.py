#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "faad2"

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("WANT_AUTOMAKE", "1.7")
    shelltools.system("sh ./bootstrap")
    autotools.configure("--with-mp4v2 \
                        --with-drm \
                        --without-xmms")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README", "README.linux", "TODO")
    pisitools.dosed("/usr/include/mpeg4ip.h", "#include <systems.h>", "#include <sys/types.h>")
