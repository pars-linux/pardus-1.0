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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "../work"

def build():
    autotools.make("SHELL=/bin/sh check")
    
def install():
    pisitools.doexe("config.sub", "/usr/share/gnuconfig")
    pisitools.doexe("config.guess", "/usr/share/gnuconfig")
    shelltools.chmod("%s/usr/share/gnuconfig/config.*" % get.installDIR())
    pisitools.dodoc("ChangeLog")
