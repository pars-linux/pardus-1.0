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

WorkDir = "db.1.85"

def build():
    shelltools.cd("PORT/linux")
    shelltools.export("CC", get.CC())
    shelltools.export("AR", get.AR())
    shelltools.export("RANLIB", get.RANLIB())
    
    autotools.make("OORG=\"%s\" prefix=/usr" % get.CFLAGS())

def install():
    shelltools.cd("PORT/linux")

    shelltools.move("libdb.a", "libdb1.a")
    pisitools.dolib_a("libdb1.a")
    
    shelltools.move("libdb.so.2", "libdb1.so.2")
    pisitools.dolib_so("libdb1.so.2")

    pisitools.dosym("libdb1.so.2", "/usr/lib/libdb1.so")
    pisitools.dosym("libdb1.so.2", "/usr/lib/libdb.so.2")
    pisitools.dosym("libdb1.so.2", "/usr/lib/libndbm.so")
    pisitools.dosym("libdb1.a", "/usr/lib/libndbm.a")

    pisitools.insinto("/usr/include/db1", "include/db.h")
    pisitools.insinto("/usr/include/db1", "include/mpool.h")

    pisitools.dosed("include/ndbm.h", "<db.h>" ,"<db1/db.h>")
    pisitools.insinto("/usr/include/db1", "include/ndbm.h")

    pisitools.dosym("db1/ndbm.h", "/usr/include/ndbm.h")
    
    shelltools.move("db_dump185", "db1_dump185")
    pisitools.dobin("db1_dump185")

    pisitools.dodoc("../../changelog", "../../README", "../../docs/*.ps")
