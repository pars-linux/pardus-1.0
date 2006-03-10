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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    # make sure python links against the current libmagic
    pisitools.dosed("python/setup.py", "(?m)^(library_dirs.*)../src", r"\1../src/.libs")

    # dont let python README kill main README
    shelltools.move("python/README", "python/README.python")
    autotools.configure("--datadir=/usr/share/misc")

def build():
    autotools.make()
    
#    shelltools.cd("python")
#    distutils.compile()
#    shelltools.cd()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "MAINT", "README")

#    shelltools.cd("python")
#    distutils.install()

#    distutils.optimize("/usr/lib/%s/site-packages/" % get.curPYTHON())

#    pkg_postinst()
#    distutils_pkg_postinst
