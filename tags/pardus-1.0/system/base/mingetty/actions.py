#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mingetty-1.00"

def build():
    autotools.make("RPM_OPTS=\"%s\"" % get.CFLAGS())

def install():
    pisitools.dosbin("mingetty", "/sbin")
    pisitools.doman("mingetty.8")

    pisitools.insinto("/usr/share/locale/tr/LC_MESSAGES", "tr.mo", "mingetty.mo")
