#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "(?m)^(DIRS = .*)", r"DIRS = libpwdb")
    pisitools.dosed("Makefile", "EXTRAS += ", "EXTRAS += %s" % get.CFLAGS())
    pisitools.dosed("default.defs", "=gcc", "=%s" % get.CC())

def build():
    autotools.make() 

def install():
    pisitools.dodir("/lib")
    pisitools.dodir("/usr/include/pwdb")
    autotools.rawInstall("INCLUDED=%s/usr/include/pwdb LIBDIR=%s/lib LDCONFIG=\"echo\"" % (get.installDIR(), get.installDIR()))
    
    libtools.preplib("/lib")
    pisitools.domove("/lib/libpwdb.a", "/usr/lib")
    libtools.gen_usr_ldscript("libpwdb.so")

    pisitools.insinto("/etc/", "conf/pwdb.conf")

    pisitools.dodoc("CHANGES", "CREDITS", "README", "*.txt")
    pisitools.dohtml("doc")
