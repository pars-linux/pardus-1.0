#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc/imlib")

def build():
    autotools.make()

def install():
    autotools.install("includedir=%s/usr/include \
                      sysconfdir=%s/etc/imlib" % (get.installDIR(), get.installDIR()))

    libtools.preplib()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS")
    pisitools.dohtml("doc")
