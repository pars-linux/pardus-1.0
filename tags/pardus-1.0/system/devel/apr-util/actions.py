#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-dbm=db42 \
                         --with-berkeley-db=/usr/include/db4.2:/usr/lib \
                         --datadir=/usr/share/apr-util-0 \
                         --with-apr=/usr \
                         --with-expat=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\" \
                          installbuilddir=/usr/share/apr-util-0/build" % get.installDIR())

    # bogus values pointing at /var/tmp/pisi/...
    pisitools.dosed("%s/usr/bin/apu-config" % get.installDIR(), \
                    "APU_SOURCE_DIR=.*", \
                    "APU_SOURCE_DIR=/usr/share/apr-util-0")
    pisitools.dosed("%s/usr/bin/apu-config" % get.installDIR(), \
                    "APU_BUILD_DIR=.*", \
                    "APU_BUILD_DIR=/usr/share/apr-util-0/build")

    pisitools.dodoc("CHANGES", "NOTICE")
