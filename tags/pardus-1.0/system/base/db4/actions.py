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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "db-4.2.52"

def setup():
    shelltools.cd("build_unix")

    libtools.gnuconfig_update()
    
    shelltools.system("../dist/configure \
                      --prefix=/usr \
                      --mandir=/usr/share/man \
                      --infodir=/usr/share/info \
                      --datadir=/usr/share \
                      --sysconfdir=/etc \
                      --localstatedir=/var/lib \
                      --libdir=/usr/lib \
                      --enable-compat185 \
                      --with-uniquename \
                      --enable-rpc \
                      --host=%s \
                      --enable-cxx \
                      --disable-tcl \
                      --disable-java \
                      --build=%s" % (get.HOST(), get.HOST()))

def build():
    shelltools.cd("build_unix")
    autotools.make()
            
def install():
    shelltools.cd("build_unix")
    autotools.install("libdir=\"%s/usr/lib\"" % get.installDIR())

    # slot all program names to avoid overwriting
    for file in shelltools.ls("%s/usr/bin/db_*" % get.installDIR()):
        sourceFile = file.replace(get.installDIR(), "")
        destinationFile = shelltools.baseName(file.replace("_", "4.2_"))
        destinationDirectory = shelltools.dirName(sourceFile)
        pisitools.domove(sourceFile, destinationDirectory, destinationFile)

    # install all headers in a slotted location
    for file in shelltools.ls("%s/usr/include/" % get.installDIR()):
        pisitools.domove("/usr/include/%s" % file, "/usr/include/db4.2")

    pisitools.dosym("/usr/include/db4.2/db.h", "/usr/include/db.h")
    pisitools.dosym("/usr/include/db4.2/db_185.h", "/usr/include/db_185.h")

    # not everybody wants this wad of documentation as it is primarily API docs
    pisitools.domove("/usr/docs/", "/usr/share/doc/%s/html/" % get.srcTAG())
    
    pisitools.domove("/usr/bin/berkeley_db_svc", "/usr/sbin/", "berkeley_db42_svc")                      
