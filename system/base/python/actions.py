#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Python-2.4.2"

def setup():
    shelltools.export("PYTHON_DISABLE_MODULES", "_tkinter")
    shelltools.export("OPT", get.CFLAGS())

    # FIXME: IPv6 not supported by kernel, fix kernel and here...
    autotools.configure("--with-fpectl \
                        --enable-shared \
                        --disable-ipv6 \
                        --infodir=/usr/share/info \
                        --mandir=/usr/share/man \
                        --with-threads \
                        --with-libc='' \
                        --enable-unicode=ucs4 \
                        --with-wctype-functions")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/")

    shelltools.export("PYTHON_DISABLE_MODULES", "_tkinter")
    shelltools.export("PYTHON_DONTCOMPILE", "0")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    shelltools.copy("Makefile.pre.in", "%s/usr/lib/python2.4/config/" % get.installDIR())

    # While we're working on the config stuff... Let's fix the OPT var
    # so that it doesn't have any opts listed in it. Prevents the problem
    # with compiling things with conflicting opts later.
    pisitools.dosed("%s/usr/lib/python2.4/config/Makefile" % get.installDIR(), "^OPT=.*", "OPT=-DNDEBUG")

    pisitools.dosym("python2.4", "/usr/bin/python")
    pisitools.dosym("python2.4", "/usr/bin/python2")
