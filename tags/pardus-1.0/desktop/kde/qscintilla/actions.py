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

WorkDir = "qscintilla-1.65-gpl-snapshot-20051103" 

def setup():
    shelltools.cd("qt/")
    
    pisitools.dosed("qscintilla.pro", "DESTDIR = \$\(QTDIR\)/lib", "DESTDIR = %s/%s/lib" % (get.installDIR(), get.qtDIR()))
    shelltools.system("qmake -o Makefile qscintilla.pro")

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "^CFLAGS   = -pipe -w -mcpu=i686 -O2 -pipe", "CFLAGS   = %s -w" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS = -pipe -w -mcpu=i686 -O2 -pipe", "CXXFLAGS = %s -w" % get.CXXFLAGS())

def install():
    pisitools.dodoc("ChangeLog", "LICENSE", "NEWS", "README")

    # execute install target of build system
    shelltools.cd("qt/")
    autotools.make("all staticlib") # there is only an install target foolish qmake

    # installs not managed by the build system
    pisitools.insinto("%s/include" % get.qtDIR(), "qextscintilla*.h")
    pisitools.insinto("%s/translations" % get.qtDIR(), "qscintilla*.qm")

    shelltools.cd("../")
    pisitools.dohtml("doc/html/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcTAG(), "doc/Scintilla/*")
