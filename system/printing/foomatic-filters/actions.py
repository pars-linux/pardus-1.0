#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ahmet AYGÜN <ahmet@zion.gen.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("/usr/bin/foomatic-gswrapper", "/usr/lib/cups/filter/foomatic-gswrapper")
    pisitools.dosym("/usr/bin/foomatic-rip", "/usr/lib/cups/filter/cupsomatic")
    pisitools.dosym("/usr/bin/foomatic-rip", "/usr/bin/lpdomatic")
