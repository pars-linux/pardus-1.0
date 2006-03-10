#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Fatih Aşıcı <fasici@linux-sevenler.org>

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    scons.make()

def install():
    shelltools.export("DESTDIR", get.installDIR())
    scons.install("prefix=%s install" % get.kdeDIR())
    pisitools.removeDir("%s/share/applnk" % get.kdeDIR())
