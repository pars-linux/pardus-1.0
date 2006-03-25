#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("docs/net-tvtime.desktop", "tvtime.png", "tvtime")
    autotools.configure("--enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

    pisitools.dohtml("docs/html")
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README")

