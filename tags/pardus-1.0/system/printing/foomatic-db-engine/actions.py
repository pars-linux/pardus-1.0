#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ahmet AYGÜN <ahmet@zion.gen.tr>
#

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("lib")
    perlmodules.configure()
    perlmodules.make()
    perlmodules.install()
