#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s datadir=/usr/share mandir=/usr/share/man infodir=/usr/share/info" % get.installDIR())

    pisitools.domove("/usr/bin/yacc", "/usr/bin", "yacc.bison")
    pisitools.remove("/usr/lib/liby.a")
                    
    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "README", "REFERENCES", "OChangeLog", "doc/FAQ")
