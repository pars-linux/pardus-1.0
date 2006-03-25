#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "\$(PREFIX)/man", "\$(PREFIX)/share/man")
    
    # bzip2 will to run itself after it has built itself which we
    # can't do if we are cross compiling.
    pisitools.dosed("Makefile", "./bzip2 -", "bzip2 -")

def build():
    autotools.make("-j2 CC=%s AR=%s RANLIB=%s -f Makefile-libbz2_so" % (get.CC(), get.AR(), get.RANLIB()))

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    pisitools.domove("/usr/bin/", "/bin/")
    
    for link in ("/bin/bunzip2", "/bin/bzcat"):
        pisitools.remove(link)
        pisitools.dosym("/bin/bzip2", link)

    pisitools.dolib("libbz2.so.1.0.2", "/lib")

    pisitools.dosym("/lib/libbz2.so.1.0.2", "/lib/libbz2.so")
    pisitools.dosym("/lib/libbz2.so.1.0.2", "/lib/libbz2.so.1")
    pisitools.dosym("/lib/libbz2.so.1.0.2", "/lib/libbz2.so.1.0")

    pisitools.dodoc("README", "CHANGES", "Y2K_INFO", "bzip2.txt", "manual.pdf", "manual.html", "manual.ps", "manual_*.html",  "README.COMPILATION.PROBLEMS")
