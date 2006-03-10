#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ahmet AYGÜN <ahmet@zion.gen.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("po/Makefile", "/usr/bin/install", "install")

def build():
    autotools.make("OPT=\"%s\" HAVE_LIBIDN=1" % get.CFLAGS())

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/man/man1")
    autotools.rawInstall("BASEDIR=\"%s\" prefix=/usr" % get.installDIR())
    pisitools.insinto("/etc/", "whois.conf")
    pisitools.dodoc("README")
