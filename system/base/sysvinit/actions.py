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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make("-C src CC=\"%s\" DISTRO=\"Pardus\" LCRYPT=\"-lcrypt\"" % (get.CC()))

def install():
    shelltools.cd("src/")
    autotools.rawInstall("DISTRO=\"Pardus\" ROOT=%s" % get.installDIR())
