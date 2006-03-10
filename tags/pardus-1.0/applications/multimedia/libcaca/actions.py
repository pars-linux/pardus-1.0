#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get


def setup():
    libtools.libtoolize("--force")
    autotools.aclocal()
    autotools.automake("--add-missing")
    autotools.autoconf()
    
    shelltools.makedirs("%s/temp" % get.curDIR())
    shelltools.export("VARTEXFONTS", "%s/temp" % get.curDIR())

    autotools.configure("--disable-doc \
                        --enable-ncurses \
                        --enable-slang \
                        --enable-imlib2 \
                        --enable-x11 \
                        --with-x \
                        --x-libraries=/usr/lib")
    
def build():
    autotools.make()

def install():
    shelltools.export("VARTEXFONTS", "")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS",\
                               "NOTES", "README", "TODO")
