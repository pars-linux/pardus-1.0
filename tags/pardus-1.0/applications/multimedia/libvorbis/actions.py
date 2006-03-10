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

def setup():
    pisitools.dosed("configure", "-mno-ieee-fp")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/lib/libvorbisfile.so.3.1.0", "/usr/lib/libvorbisfile.so.0")
    pisitools.dosym("/usr/lib/libvorbisenc.so.2.0.0", "/usr/lib/libvorbisenc.so.0")

    pisitools.removeDir("/usr/share/doc")
    pisitools.dodoc("AUTHORS", "README", "todo.txt", "doc/*.txt")
    pisitools.dohtml("doc")
