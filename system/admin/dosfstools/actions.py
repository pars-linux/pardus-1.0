#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "PREFIX\ \=", "PREFIX\ \=\ \/usr")
    pisitools.dosed("Makefile", "\/usr\/man", "\/share\/man")

def build():
    # this package does *not* play well with optimisations
    # maybe we should define some static CFLAGS
    autotools.make()

def install():
    autotools.install("PREFIX=%s/usr" % get.installDIR())
    pisitools.dodoc("CHANGES", "TODO")
    pisitools.newdoc("dosfsck/README", "README.dosfsck")
    pisitools.newdoc("dosfsck/CHANGES", "CHANGES.dosfsck")
    pisitools.newdoc("dosfsck/COPYING", "COPYING.dosfsck")
    pisitools.newdoc("mkdosfs/README", "README.mkdosfs")
    pisitools.newdoc("mkdosfs/ChangeLog", "ChangeLog.mkdosfs")

