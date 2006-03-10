#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "esvn"

def setup():
    # pisitools.dosed("esvn.pro", "/usr/share/pixmaps", "/usr/share/icons")
    pisitools.dosed("src/mainwindow.cpp", "/usr/share/doc/esvn/html-docs", "/usr/share/doc/esvn-0.6.11-1/html")

def build():
    shelltools.export("QTDIR", get.qtDIR())
    autotools.make()

def install():
    autotools.rawInstall("-f esvn.mak INSTALL_ROOT=%s install" % get.installDIR())
    pisitools.dobin("esvn")
    pisitools.dobin("esvn-diff-wrapper")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
    pisitools.dohtml("html-docs/*")

