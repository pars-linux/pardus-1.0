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
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Re-generate ltmain.sh, configure and friends, since the upstream tarball
    # was built with a buggy libtool (missing 'so' extension in binaries).
    shelltools.export("WANT_AUTOMAKE", "1.7")
    libtools.libtoolize("--copy --force")
    autotools.aclocal("-I .")
    autotools.autoconf()
    autotools.configure("--disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
