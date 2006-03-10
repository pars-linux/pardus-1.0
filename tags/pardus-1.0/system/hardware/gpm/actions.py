#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@haftalik.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.configure("--libdir=/lib --sysconfdir=/etc/gpm")

def build():
    autotools.make("CC=%s AR=%s RANLIB=%s" % (get.CC(), get.AR(), get.RANLIB()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("libgpm.so.1.19.0", "/lib/libgpm.so.1")
    pisitools.dosym("libgpm.so.1", " /lib/libgpm.so")

    pisitools.dodir("/usr/lib")
    pisitools.domove("/lib/*.a", "/usr/lib/")
    libtools.gen_usr_ldscript("libgpm.so")

    pisitools.insinto("/etc/gpm", "conf/gpm-*.conf")

    pisitools.dodoc("BUGS", "Changes", "README", "TODO", "doc/Announce", "doc/FAQ", "doc/README*")
