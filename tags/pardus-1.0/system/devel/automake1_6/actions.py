#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "automake-1.6.3"

def setup():
    pisitools.dosed("automake.texi", "(?m)^(@setfilename.*)automake", r"\1automake1.6")
    pisitools.dosed("automake.texi", "automake: (automake)", "automake v1.6: (automake1.6)")
    pisitools.dosed("automake.texi", "aclocal: (automake)", "aclocal v1.6: (automake1.6)")

    shelltools.export("WANT_AUTOCONF", "2.5")                    
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
   
    pisitools.remove("/usr/bin/aclocal")
    pisitools.remove("/usr/bin/automake")
                    
    pisitools.dodoc("NEWS", "README", "THANKS", "TODO", "AUTHORS", "ChangeLog")
    pisitools.doinfo("*.info")

    # remove all config.guess and config.sub files replacing them
    # w/a symlink to a specific gnuconfig version
    for suffix in ("guess", "sub"):
        pisitools.remove("/usr/share/automake-1.6/config.%s" % suffix)
        pisitools.dosym("../gnuconfig/config.%s" % suffix, "/usr/share/automake-1.6/config.%s" % suffix)
