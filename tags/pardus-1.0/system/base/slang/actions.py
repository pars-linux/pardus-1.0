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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("all elf")

def install():
    autotools.rawInstall("install-elf DESTDIR=%s" % get.installDIR())

    shelltools.chmod("%s/usr/lib/libslang.so.*" % get.installDIR(), 0755)

    for file in shelltools.ls("%s/usr/lib/libslang-utf8*" % get.installDIR()):
        libslangutf8 = file.replace(get.installDIR(), "")
        libslang = libslangutf8.replace("-utf8", "")
        pisitools.dosym(libslangutf8, libslang)
        print libslangutf8, libslang

    # remove the documentation... we want to install it ourselves
    pisitools.removeDir("/usr/doc")
    pisitools.dodoc("COPYING*", "NEWS", "README", "*.txt", "doc/*.txt", "doc/internal/*.txt", "doc/text/*.txt")
    pisitools.dohtml("doc/")
