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
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Inject our own CFLAGS / docpath

    pisitools.dosed("include/builddefs.in", "GCFLAGS = -O1", "GCFLAGS = ")
    pisitools.dosed("include/builddefs.in", "PKG_DOC_DIR =.*", "PKG_DOC_DIR = /usr/share/doc/%s" % get.srcTAG())
    
    # ugly hack to replace flags -O[2-9] -> -O1
    a = get.CFLAGS()
    if a.find("-O") is not -1:
        flags = a[:a.find("-O")] + " -O1 " + a[a.find("-O")+4:]
    else:
        flags = a + " -O1"

    shelltools.export("CFLAGS", flags)

    # These two craps are probably needed for different platforms, but they break 
    # our current build so they are commented
    
    # make sure the PLATFORM envvar doesn't break crap
    #pisitools.dosed("configure", "PLATFORM", "")

    # We'll handle /lib versus /usr/lib install
    #pisitools.dosed("include/buildmacros", "INSTALL.* -S .*LIBNAME")

    shelltools.export("OPTIMIZER", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.configure("--bindir=/bin --sbindir=/sbin --libexecdir=/usr/lib  --enable-gettext")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DIST_ROOT=\"%s\" install-dev" % get.installDIR())

    # shared in /lib, static in /usr/lib, ldscript fun too
    pisitools.domove("/usr/lib/lib*.so*", "/lib")
    libtools.gen_usr_ldscript("libhandle.so")


