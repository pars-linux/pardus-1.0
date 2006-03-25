#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "perl-5.8.7"

def setup():
    shelltools.export("LC_ALL", "C") 

    shelltools.system("sh Configure -des \
                      -Darchname=i686-linux \
                      -Dcccdlflags=-fPIC \
                      -Dccdlflags=-rdynamic \
                      -Dcc=%s \
                      -Dprefix=/usr \
                      -Dvendorprefix=/usr \
                      -Dsiteprefix=/usr \
                      -Ulocincpth=  \
                      -Doptimize=\"%s\" \
                      -Duselargefiles \
                      -Duseshrplib \
                      -Dman3ext=3pm \
                      -Dlibperl=libperl.so.1.5.8 \
                      -Dd_dosuid \
                      -Dd_semctl_semun \
                      -Dcf_by=Pardus \
                      -Ud_csh \
                      -Di_gdbm \
                      -Di_db \
                      -Di_ndbm" % (get.CC(), get.CFLAGS()))

def build():
    autotools.make("-j1 -f Makefile depend")
    autotools.make("-j1 -f Makefile libperl.so.1.5.8")

def install():
    pisitools.dolib("libperl.so.1.5.8")
    libtools.preplib()
    
    pisitools.dodoc("Changes*", "Artistic", "Copying", "README", "Todo*", "AUTHORS")
