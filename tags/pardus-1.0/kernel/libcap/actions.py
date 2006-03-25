#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Make.Rules", "WARNINGS=-ansi", "WARNINGS=")

def build():
    autotools.make("COPTFLAG=\"%s\" \
                    LDFLAGS=\"%s\" \
                    DEBUG=\"\"" % (get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall("FAKEROOT=\"%(installDIR)s\" \
                          man_prefix=/usr/share \
                          LIBDIR=%(installDIR)s/lib \
                          " % {'installDIR': get.installDIR()})

    # Move libcap.a to /usr/lib
    pisitools.dodir("/usr/lib")
    pisitools.domove("/lib/libcap.a", "/usr/lib")

    # Libs
    libtools.gen_usr_ldscript("libcap.so")
    
    # Docs
    pisitools.dodoc("CHANGELOG", "README", "pgp.keys.asc", "doc/capability.notes", "capfaq-0.2.txt")
