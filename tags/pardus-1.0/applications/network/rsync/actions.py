#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-rsyncd-conf=/etc/rsyncd.conf")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

    pisitools.dodoc("NEWS", "OLDNEWS", "README", "TODO", "tech_report.tex")
