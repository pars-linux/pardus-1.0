#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.make("-f admin/Makefile.common")
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/lib/nsbrowser/plugins")
    shelltools.copy("dragonegg/.libs/libdragonegg.so","%s/usr/lib/nsbrowser/plugins/" % get.installDIR())
