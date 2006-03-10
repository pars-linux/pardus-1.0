#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Build with --without-included-gettext (will use that of glibc), as we
    # need preloadable_libintl.so for new help2man
    shelltools.export("CXX", get.CXX())
    autotools.configure("--without-java --without-included-gettext --enable-nls")

def build():
    autotools.make()

def install():
    autotools.install("lispdir=%s/usr/share/emacs/site-lisp docdir=%s/usr/share/doc/%s/html" % (get.installDIR(), get.installDIR(), get.srcTAG()))

    pisitools.dosym("msgfmt", "/usr/bin/gmsgfmt")
    pisitools.doexe("gettext-tools/misc/gettextize", "/usr/bin")

    pisitools.domove("/usr/doc/gettext", "/usr/share/doc/%s/html" % get.srcTAG())

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "DISCLAIM", "NEWS", "README*", "THANKS", "TODO")
