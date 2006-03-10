#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde

def setup():
    shelltools.export("MAKE_PO", "bg ca br da de cs cy el es et fi ga fr gl hu is it lt nb mt nl pa pl pt ro ru rw ta sr sv tr en_GB pt_BR zh_CN sr@Latn")
    shelltools.export("MAKE_DOC", "da et fr it nl pt ru sv")

    pisitools.dosed("po/Makefile.in", "^SUBDIRS =.*", "SUBDIRS = %s" % get.ENV("MAKE_PO"))
    pisitools.dosed("doc/Makefile.in", "^SUBDIRS =.*", "SUBDIRS = . %s kdetv" % get.ENV("MAKE_DOC"))

    kde.configure("--enable-arts")

def build():
    kde.make()

def install():
    kde.install()

