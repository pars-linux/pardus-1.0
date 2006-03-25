#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.touch("man/*.1")
    shelltools.chmod("config/*", 0775)
    
    autotools.configure("--enable-nls")
    
def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "NEWS", "README")

    # use the manpage from man-pages
    pisitools.remove("/usr/share/man/man1/diff.1")
