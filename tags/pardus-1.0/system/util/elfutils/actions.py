#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


dirs = ["", "m4/", "lib/", "libelf/", "doc/", "libebl/", \
        "libdw/", "libcpu/", "libasm/", "src/", "tests/"]

def setup():
    for dir in dirs:
        pisitools.dosed("%sMakefile.in" % dir, "-Werror", "")

    autotools.configure('--program-prefix="eu-" \
                         --enable-shared \
                         --enable-nls') 

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 

    pisitools.remove("/usr/bin/eu-ld")

    for file in ["libasm", "libdw", "libdwarf"]:
        pisitools.remove("/usr/include/elfutils/%s.h" % file)
        pisitools.remove("/usr/lib/%s.a" % file)

    pisitools.remove("/usr/lib/libasm.so*")
    pisitools.remove("/usr/lib/libasm-0.94.so")
    pisitools.removeDir("/usr/usr")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS",\
                    "NOTES", "README", "THANKS", "TODO")
