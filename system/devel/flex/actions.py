#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "flex-2.5.4"

def setup():
    autotools.rawConfigure("--prefix=/usr --host=%s" % get.HOST())

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("prefix=%s/usr mandir=%s/usr/share/man/man1" % (get.installDIR(), get.installDIR()))
    pisitools.dodoc("NEWS", "README")
    pisitools.dosym("flex", "/usr/bin/lex")
