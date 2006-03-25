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

def setup():
    libtools.gnuconfig_update()
    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README", "TODO", "INSTALL")
