#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Eray Özkural <eray@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.util import join_path as join

WorkDir="boost_1_33_1"

def setup():
    autotools.rawConfigure("--prefix=/usr --with-python=python")

def build():
    autotools.make()

def install():
    shelltools.system("./tools/build/jam_src/bin.linuxx86/bjam --prefix=%s install" % 
                      join(get.installDIR(), "usr"))
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")
