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

def setup():
    autotools.configure("--with-posix-regex \
                         --without-readlib \
                         --disable-etags \
                         --enable-tmpdir=/tmp")

def build():
    autotools.make()

def install():
    autotools.install()
    
    # Emacs paketinden gelen ctags ile karışmasın...
    pisitools.domove("/usr/bin/ctags", "/usr/bin", "exuberant-ctags")
    pisitools.domove("/usr/share/man/man1/ctags.1", "/usr/share/man/man1", "exuberant-ctags.1")

    pisitools.dodoc("FAQ", "NEWS", "README")
    pisitools.dohtml("EXTENDING.html", "ctags.html")
