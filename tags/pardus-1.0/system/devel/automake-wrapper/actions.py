#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "automake-wrapper"

def install():
    pisitools.dodir("/usr/lib/misc/")
    pisitools.dodir("/usr/share/aclocal")
    
    pisitools.doexe("am-wrapper.sh", "/usr/lib/misc/")

    pisitools.dosym("../lib/misc/am-wrapper.sh", "/usr/bin/automake")
    pisitools.dosym("../lib/misc/am-wrapper.sh", "/usr/bin/aclocal")
