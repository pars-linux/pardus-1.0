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

def build():
    autotools.make()

def install():
    pisitools.dobin("tempfile", "/bin")
    pisitools.dobin("mktemp", "/bin")
    pisitools.dobin("run-parts", "/bin")

    pisitools.doexe("savelog", "/usr/sbin")

    pisitools.dosbin("installkernel", "/sbin")
    pisitools.dosbin("mkboot")

    pisitools.doman("mktemp.1", "tempfile.1", "run-parts.8", "savelog.8", "installkernel.8", "mkboot.8")
    pisitools.dodoc("debian/changelog", "debian/control")
