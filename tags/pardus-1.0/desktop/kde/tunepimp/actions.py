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
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "libtunepimp-0.3.0"

def setup():
    # do not try to link against obsolete libtermcap
    pisitools.dosed("configure", "-ltermcap", "-lncurses")            
    
    autotools.configure()
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "README", "TODO")

    shelltools.cd("python/")
    pythonmodules.install()
    pisitools.insinto("/usr/share/doc/%s/examples/" % get.srcTAG(), "examples/*")
