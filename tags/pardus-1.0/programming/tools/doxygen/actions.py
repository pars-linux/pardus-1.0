#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "^\(TMAKE_CFLAGS_RELEASE\t*\)= .*$", "\1= %s" % get.CFLAGS())
    pisitools.dosed("tmake/lib/linux-g++/tmake.conf", "^\(TMAKE_CXXFLAGS_RELEASE\t*\)= .*$", "\1= %s" % get.CXXFLAGS())

    autotools.rawConfigure("--prefix %s/usr --with-doxywizard" % get.installDIR())

def build():
    autotools.make("DESTDIR=%s all" % get.installDIR())

def install():
    autotools.install()
    pisitools.dodoc("INSTALL", "LANGUAGE.HOWTO", "LICENSE", "README", "VERSION")
