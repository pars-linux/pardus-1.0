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
# Timu EREN <selamtux@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pccts"

def build():
    autotools.make("COPT=\"%s\"" % get.CFLAGS())
    
def install():
    # main binaries
    pisitools.dobin("bin/antlr")
    pisitools.dobin("bin/dlg")
    pisitools.dobin("bin/genmk")
    pisitools.dobin("bin/sor")
    
    # main includes
    pisitools.insinto("/usr/include/pccts","h/*.h")
    pisitools.insinto("/usr/include/pccts","h/*.c")
    pisitools.insinto("/usr/include/pccts","h/*.cpp")

    # sorcerer includs
    pisitools.insinto("/usr/include/pccts/sorcerer","sorcerer/h/*.h")
    pisitools.insinto("/usr/include/pccts/sorcerer","sorcerer/h/*.c")
    pisitools.insinto("/usr/include/pccts/sorcerer","sorcerer/h/*.cpp")
    
    # sorcerer includes
    pisitools.insinto("/usr/include/pccts/sorcerer/lib","sorcerer/lib/*.h")
    pisitools.insinto("/usr/include/pccts/sorcerer/lib","sorcerer/lib/*.c")
    pisitools.insinto("/usr/include/pccts/sorcerer/lib","sorcerer/lib/*.cpp")
    
    pisitools.dodoc("CHANGES*", "KNOWN_PROBLEMS*", "README", "RIGHTS", "history.txt", "history.ps")
    pisitools.dodoc("sorcerer/README", "sorcerer/UPDATES")
    
    pisitools.doman("dlg/dlg.1", "antlr/antlr.1")
