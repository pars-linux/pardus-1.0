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

WorkDir = "autoconf-2.13"

def setup():
    # make sure configure is newer than configure.in
    shelltools.touch("configure")

    pisitools.dosed("autoconf.texi", "\* Autoconf:", "\* Autoconf v2.1:")
    pisitools.dosed("autoconf.texi", "START-INFO-DIR-ENTRY"," i INFO-DIR-SECTION GNU programming tools")

    autotools.configure("--exec-prefix=/usr --bindir=/usr/bin --program-suffix=\"-2.13\"")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO", "ChangeLog", "ChangeLog.0", "ChangeLog.1")
    pisitools.domove("/usr/share/info/autoconf.info", "/usr/share/info/", "autoconf-2.13.info")
    
    # binutils installs this infopage
    pisitools.remove("/usr/share/info/standards.info")
