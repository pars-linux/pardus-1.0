#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "autoconf-wrapper"

def install():
    pisitools.dodir("/usr/lib/misc/")

    pisitools.doexe("ac-wrapper.sh", "/usr/lib/misc/")

    for file in ("autoconf", "autom4te", "autoscan", "autoheader", "autoreconf", "autoupdate", "ifnames"):
        pisitools.dosym("../lib/misc/ac-wrapper.sh", "/usr/bin/%s" % file)
