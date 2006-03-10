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

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())

    # many fun sandbox errors, phhh
    autotools.rawConfigure("--host=%s --prefix=/usr --mandir=/usr/share/man \
                           --infodir=%s/usr/share/info" % (get.HOST(), get.installDIR()))

def build():
    autotools.make("-j1")

def install():
    pisitools.dodir("/usr")
    pisitools.dodir("/usr/share/doc/%s/examples" % get.srcTAG())
    pisitools.dodir("/usr/share/doc/%s/html" % get.srcTAG())

    autotools.rawInstall("prefix=%s/usr manroot=%s/usr/share/man inforoot=%s/usr/share/info \
                         docdir=%s/usr/share/doc/%s" % (get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR(), get.srcTAG()))

    # The following links are required for xman
    pisitools.dosym("eqn", "/usr/bin/geqn")
    pisitools.dosym("tbl", "/usr/bin/gtbl")
    pisitools.dosym("soelim", "/usr/bin/zsoelim")

    pisitools.dodoc("BUG-REPORT", "ChangeLog", "FDL", "MORE.STUFF", "NEWS", "PROBLEMS", "PROJECTS", "README", "REVISION", "TODO", "VERSION")
